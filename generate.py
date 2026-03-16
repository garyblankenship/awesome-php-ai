#!/usr/bin/env python3
"""Generate README.md from readme.json."""

import json
from pathlib import Path

SECTIONS = [
    {
        "key": "llm_frameworks",
        "title": "LLM Frameworks",
        "level": 2,
        "description": "Full-featured frameworks for building LLM-powered applications.",
        "in_toc": True,
    },
    {
        "key": "llm_clients_adapters",
        "title": "LLM Clients & Adapters",
        "level": 2,
        "description": "Client libraries and provider integrations.",
        "in_toc": True,
    },
    {
        "key": None,
        "title": "Natural Language Processing",
        "level": 2,
        "in_toc": True,
        "children": [
            {
                "key": "structured_output",
                "title": "Structured Output & Validation",
                "level": 3,
            },
            {
                "key": "ai_agents_orchestration",
                "title": "AI Agents & Orchestration",
                "level": 3,
            },
            {
                "key": "laravel_integrations",
                "title": "Laravel Integrations",
                "level": 3,
            },
            {
                "key": "symfony_integrations",
                "title": "Symfony Integrations",
                "level": 3,
            },
            {
                "key": "utilities_tools",
                "title": "Utilities & Tools",
                "level": 3,
            },
        ],
    },
    {
        "key": "machine_learning",
        "title": "Machine Learning",
        "level": 2,
        "in_toc": True,
    },
    {
        "key": "computer_vision",
        "title": "Computer Vision",
        "level": 2,
        "in_toc": True,
    },
    {
        "key": "vector_storage_rag",
        "title": "Vector Storage & RAG",
        "level": 2,
        "in_toc": True,
    },
    {
        "key": "command_line_tools",
        "title": "Command Line Tools",
        "level": 2,
        "in_toc": True,
    },
    {
        "key": "video_processing",
        "title": "Video Processing",
        "level": 2,
        "in_toc": True,
    },
    {
        "key": "api_clients",
        "title": "API Clients",
        "level": 2,
        "in_toc": True,
    },
    {
        "key": "learning_resources",
        "title": "Learning Resources",
        "level": 2,
        "in_toc": True,
        "suffix": "\n### Tutorials & Documentation\n\n- [Fun With OpenAI and Laravel](https://laracasts.com/series/fun-with-openai-and-laravel) - Laracasts series on OpenAI with PHP and Laravel.\n- [PHP-ML Tutorials](https://php-ml.readthedocs.io/en/latest/tutorials/) - Learn how to use PHP-ML for machine learning.\n- [Rubix ML Docs](https://docs.rubixml.com/) - Comprehensive documentation for Rubix ML.",
    },
    {
        "key": "data_manipulation",
        "title": "Data Manipulation",
        "level": 2,
        "in_toc": False,
    },
]

HEADER = """\
# Awesome PHP AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome PHP libraries and tools for AI, Machine Learning, and Natural Language Processing.

Contributions welcome! Read the [contributing guidelines](#contributing) to get started."""

FOOTER = """\
## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Add your library/tool to the appropriate section
3. Include the library name, GitHub link, and a brief description
4. Submit a pull request

Please ensure your submission is relevant to PHP and AI/ML/NLP.

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work."""


SITE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awesome PHP AI</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        gray: {
                            950: '#0a0a0f',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #111827; }
        ::-webkit-scrollbar-thumb { background: #374151; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #4b5563; }

        .tag-provider        { background: rgba(30,58,138,0.5); color: #93c5fd; border-color: #1d4ed8; }
        .tag-provider.active { background: #1d4ed8; color: #fff; border-color: #3b82f6; }
        .tag-feature         { background: rgba(88,28,135,0.5); color: #d8b4fe; border-color: #7e22ce; }
        .tag-feature.active  { background: #7e22ce; color: #fff; border-color: #a855f7; }
        .tag-framework       { background: rgba(20,83,45,0.5); color: #86efac; border-color: #166534; }
        .tag-framework.active{ background: #166534; color: #fff; border-color: #22c55e; }
        .tag-type            { background: #1f2937; color: #9ca3af; border-color: #4b5563; }
        .tag-type.active     { background: #4b5563; color: #fff; border-color: #6b7280; }

        .pill-btn { transition: all 0.15s ease; }
        .pill-btn.active { background: #2563eb; color: #fff; border-color: #3b82f6; }

        .card { transition: border-color 0.2s ease, transform 0.2s ease; }
        .card:hover { transform: translateY(-1px); }
    </style>
</head>
<body class="bg-gray-950 text-gray-100 min-h-screen">

    <!-- Header -->
    <header class="border-b border-gray-800 bg-gray-900/50 backdrop-blur-sm sticky top-0 z-10">
        <div class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
            <div>
                <h1 class="text-2xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                    Awesome PHP AI
                </h1>
                <p class="text-gray-400 text-sm mt-0.5">Curated PHP libraries for AI, ML &amp; NLP</p>
            </div>
            <a href="https://github.com/garyblankenship/awesome-php-ai"
               target="_blank"
               class="flex items-center gap-2 text-sm text-gray-400 hover:text-white border border-gray-700 hover:border-gray-500 rounded-lg px-3 py-2 transition-colors">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
                </svg>
                GitHub
            </a>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 py-8">

        <!-- Stats bar -->
        <div class="grid grid-cols-3 gap-4 mb-8">
            <div class="bg-gray-900 border border-gray-800 rounded-xl p-4 text-center">
                <div id="stat-entries" class="text-3xl font-bold text-blue-400">—</div>
                <div class="text-gray-500 text-sm mt-1">Libraries</div>
            </div>
            <div class="bg-gray-900 border border-gray-800 rounded-xl p-4 text-center">
                <div id="stat-stars" class="text-3xl font-bold text-yellow-400">—</div>
                <div class="text-gray-500 text-sm mt-1">Total Stars</div>
            </div>
            <div class="bg-gray-900 border border-gray-800 rounded-xl p-4 text-center">
                <div id="stat-categories" class="text-3xl font-bold text-purple-400">—</div>
                <div class="text-gray-500 text-sm mt-1">Categories</div>
            </div>
        </div>

        <!-- Search -->
        <div class="mb-4">
            <input id="search"
                   type="text"
                   placeholder="Search libraries..."
                   class="w-full bg-gray-900 border border-gray-700 rounded-xl px-4 py-3 text-gray-100 placeholder-gray-500 focus:outline-none focus:border-blue-500 transition-colors text-sm">
        </div>

        <!-- Controls row -->
        <div class="flex flex-wrap items-center gap-3 mb-4">
            <!-- Sort toggle -->
            <div class="flex gap-1 bg-gray-900 border border-gray-800 rounded-lg p-1">
                <button id="sort-stars" class="pill-btn active text-xs px-3 py-1.5 rounded-md font-medium">
                    Stars
                </button>
                <button id="sort-alpha" class="pill-btn text-xs px-3 py-1.5 rounded-md font-medium text-gray-400 hover:text-white">
                    A–Z
                </button>
            </div>

            <!-- Category pills -->
            <div id="category-pills" class="flex flex-wrap gap-1.5"></div>
        </div>

        <!-- Tag filters (collapsible) -->
        <div class="mb-6">
            <button id="toggle-tags" class="text-xs text-gray-500 hover:text-gray-300 flex items-center gap-1 mb-3 transition-colors">
                <svg id="toggle-arrow" class="w-3 h-3 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                </svg>
                Filter by tags
            </button>
            <div id="tag-filters" class="hidden">
                <div id="tag-groups" class="space-y-3"></div>
            </div>
        </div>

        <!-- Results count -->
        <div id="results-count" class="text-xs text-gray-500 mb-4"></div>

        <!-- Card grid -->
        <div id="card-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4"></div>

        <!-- Empty state -->
        <div id="empty-state" class="hidden text-center py-20 text-gray-600">
            <div class="text-5xl mb-4">&#128269;</div>
            <div class="text-lg">No libraries found</div>
            <div class="text-sm mt-1">Try different search terms or filters</div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="border-t border-gray-800 mt-16 py-8 text-center text-gray-600 text-sm">
        <a href="https://github.com/garyblankenship/awesome-php-ai" target="_blank" class="hover:text-gray-400 transition-colors">
            awesome-php-ai
        </a>
        &mdash; CC0 Public Domain
    </footer>

<script>
const DATA = {{ENTRIES_JSON}};

const CATEGORIES = {
    llm_frameworks: "LLM Frameworks",
    llm_clients_adapters: "LLM Clients & Adapters",
    structured_output: "Structured Output",
    ai_agents_orchestration: "AI Agents & Orchestration",
    laravel_integrations: "Laravel Integrations",
    symfony_integrations: "Symfony Integrations",
    utilities_tools: "Utilities & Tools",
    machine_learning: "Machine Learning",
    computer_vision: "Computer Vision",
    vector_storage_rag: "Vector Storage & RAG",
    command_line_tools: "Command Line Tools",
    video_processing: "Video Processing",
    api_clients: "API Clients",
    learning_resources: "Learning Resources",
    data_manipulation: "Data Manipulation"
};

const TAG_GROUPS = {
    Providers: ["openai","anthropic","google","ollama","mistral","cohere","deepseek","grok","fireworks","openrouter","huggingface"],
    Features: ["streaming","tool-use","embeddings","rag","agents","structured-output","image-generation","vision","text-to-speech","chat","mcp","nlp","machine-learning","search","translation","video","subtitles","slugify"],
    Frameworks: ["laravel","symfony"],
    Types: ["framework","client","library","tool","cli","example","book","bundle"]
};

const TAG_GROUP_MAP = {};
for (const [group, tags] of Object.entries(TAG_GROUPS)) {
    for (const tag of tags) TAG_GROUP_MAP[tag] = group;
}

function tagClass(tag, active) {
    const group = TAG_GROUP_MAP[tag] || 'Types';
    const base = {
        Providers:  'tag-provider',
        Features:   'tag-feature',
        Frameworks: 'tag-framework',
        Types:      'tag-type',
    }[group] || 'tag-type';
    return base + (active ? ' active' : '');
}

// Flatten DATA into array
const ALL_ENTRIES = [];
for (const [catKey, entries] of Object.entries(DATA)) {
    for (const e of entries) {
        ALL_ENTRIES.push({ ...e, category: catKey });
    }
}

// Compute tag counts
const tagCounts = {};
for (const e of ALL_ENTRIES) {
    for (const t of (e.tags || [])) {
        tagCounts[t] = (tagCounts[t] || 0) + 1;
    }
}

// State
let state = {
    search: '',
    category: 'all',
    tags: new Set(),
    sort: 'stars',
};

function filtered() {
    let res = ALL_ENTRIES;
    if (state.search) {
        const q = state.search.toLowerCase();
        res = res.filter(e =>
            e.name.toLowerCase().includes(q) ||
            (e.description || '').toLowerCase().includes(q)
        );
    }
    if (state.category !== 'all') {
        res = res.filter(e => e.category === state.category);
    }
    if (state.tags.size > 0) {
        res = res.filter(e => {
            const et = new Set(e.tags || []);
            for (const t of state.tags) if (!et.has(t)) return false;
            return true;
        });
    }
    if (state.sort === 'stars') {
        res = [...res].sort((a, b) => (b.stars || 0) - (a.stars || 0));
    } else {
        res = [...res].sort((a, b) => a.name.localeCompare(b.name));
    }
    return res;
}

function starIcon() {
    return '<svg class="inline w-3.5 h-3.5 mb-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>';
}

function categoryBadge(catKey) {
    const label = CATEGORIES[catKey] || catKey;
    return `<span class="text-xs px-2 py-0.5 rounded-full bg-gray-800 text-gray-400 border border-gray-700">${label}</span>`;
}

function renderCard(e) {
    const tagPills = (e.tags || []).map(t =>
        `<span class="tag-chip text-xs px-1.5 py-0.5 rounded border ${tagClass(t, false)}">${t}</span>`
    ).join(' ');

    return `<div class="card bg-gray-900 border border-gray-800 rounded-xl p-5 hover:border-blue-500/50 flex flex-col gap-3">
        <div class="flex items-start justify-between gap-2">
            <div class="flex flex-col gap-1.5">
                ${categoryBadge(e.category)}
                <a href="${e.url}" target="_blank" class="text-blue-400 font-semibold text-lg hover:underline leading-tight">${e.name}</a>
            </div>
            <span class="text-yellow-400 text-sm whitespace-nowrap font-medium flex items-center gap-0.5 mt-1 shrink-0">
                ${starIcon()}
                ${(e.stars || 0).toLocaleString()}
            </span>
        </div>
        <p class="text-gray-400 text-sm leading-relaxed flex-1">${e.description || ''}</p>
        <div class="flex flex-wrap gap-1">${tagPills}</div>
    </div>`;
}

function render() {
    const res = filtered();
    const grid = document.getElementById('card-grid');
    const empty = document.getElementById('empty-state');
    const count = document.getElementById('results-count');

    if (res.length === 0) {
        grid.innerHTML = '';
        empty.classList.remove('hidden');
    } else {
        empty.classList.add('hidden');
        grid.innerHTML = res.map(renderCard).join('');
    }

    count.textContent = `Showing ${res.length.toLocaleString()} of ${ALL_ENTRIES.length.toLocaleString()} libraries`;

    // Update category pills active state
    document.querySelectorAll('.cat-pill').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.cat === state.category);
    });

    // Update sort buttons
    document.getElementById('sort-stars').classList.toggle('active', state.sort === 'stars');
    document.getElementById('sort-stars').classList.toggle('text-gray-400', state.sort !== 'stars');
    document.getElementById('sort-alpha').classList.toggle('active', state.sort === 'alpha');
    document.getElementById('sort-alpha').classList.toggle('text-gray-400', state.sort !== 'alpha');

    // Update tag chips active state
    document.querySelectorAll('.tag-filter-chip').forEach(btn => {
        const tag = btn.dataset.tag;
        const active = state.tags.has(tag);
        btn.className = `tag-filter-chip text-xs px-2 py-1 rounded border cursor-pointer transition-colors ${tagClass(tag, active)}`;
    });
}

function initStats() {
    const totalStars = ALL_ENTRIES.reduce((s, e) => s + (e.stars || 0), 0);
    const catKeys = new Set(ALL_ENTRIES.map(e => e.category));
    document.getElementById('stat-entries').textContent = ALL_ENTRIES.length.toLocaleString();
    document.getElementById('stat-stars').textContent = totalStars.toLocaleString();
    document.getElementById('stat-categories').textContent = catKeys.size;
}

function initCategoryPills() {
    const container = document.getElementById('category-pills');
    const cats = [...new Set(ALL_ENTRIES.map(e => e.category))];

    const allBtn = document.createElement('button');
    allBtn.className = 'cat-pill pill-btn active text-xs px-3 py-1.5 rounded-lg border border-gray-700 bg-gray-900 hover:border-gray-500 font-medium';
    allBtn.dataset.cat = 'all';
    allBtn.textContent = 'All';
    allBtn.addEventListener('click', () => { state.category = 'all'; render(); });
    container.appendChild(allBtn);

    for (const cat of cats) {
        const btn = document.createElement('button');
        btn.className = 'cat-pill pill-btn text-xs px-3 py-1.5 rounded-lg border border-gray-700 bg-gray-900 hover:border-gray-500 text-gray-400 hover:text-white font-medium';
        btn.dataset.cat = cat;
        btn.textContent = CATEGORIES[cat] || cat;
        btn.addEventListener('click', () => { state.category = cat; render(); });
        container.appendChild(btn);
    }
}

function initTagGroups() {
    const container = document.getElementById('tag-groups');
    for (const [groupName, tags] of Object.entries(TAG_GROUPS)) {
        const existing = tags.filter(t => tagCounts[t]);
        if (!existing.length) continue;

        const row = document.createElement('div');
        row.className = 'flex flex-wrap items-center gap-2';

        const label = document.createElement('span');
        label.className = 'text-xs text-gray-600 w-20 shrink-0';
        label.textContent = groupName;
        row.appendChild(label);

        const chips = document.createElement('div');
        chips.className = 'flex flex-wrap gap-1.5';
        for (const tag of existing) {
            const btn = document.createElement('button');
            btn.className = `tag-filter-chip text-xs px-2 py-1 rounded border cursor-pointer transition-colors ${tagClass(tag, false)}`;
            btn.dataset.tag = tag;
            btn.textContent = `${tag} (${tagCounts[tag]})`;
            btn.addEventListener('click', () => {
                if (state.tags.has(tag)) state.tags.delete(tag);
                else state.tags.add(tag);
                render();
            });
            chips.appendChild(btn);
        }
        row.appendChild(chips);
        container.appendChild(row);
    }
}

function initToggleTags() {
    const btn = document.getElementById('toggle-tags');
    const panel = document.getElementById('tag-filters');
    const arrow = document.getElementById('toggle-arrow');
    btn.addEventListener('click', () => {
        const hidden = panel.classList.toggle('hidden');
        arrow.style.transform = hidden ? '' : 'rotate(90deg)';
    });
}

function initSearch() {
    document.getElementById('search').addEventListener('input', e => {
        state.search = e.target.value;
        render();
    });
}

function initSort() {
    document.getElementById('sort-stars').addEventListener('click', () => { state.sort = 'stars'; render(); });
    document.getElementById('sort-alpha').addEventListener('click', () => { state.sort = 'alpha'; render(); });
}

// Boot
initStats();
initCategoryPills();
initTagGroups();
initToggleTags();
initSearch();
initSort();
render();
</script>
</body>
</html>
"""


def build_toc(sections: list[dict]) -> str:
    lines = []
    for section in sections:
        if section.get("in_toc"):
            anchor = section["title"].lower().replace("&", "").replace(" ", "-")
            lines.append(f"- [{section['title']}](#{anchor})")
    return "## Table of Contents\n\n" + "\n".join(lines)


def render_table(entries: list[dict]) -> str:
    lines = [
        "| Repo | Description |",
        "|---------|-------------|",
    ]
    for entry in entries:
        lines.append(
            f"| [{entry['name']}]({entry['url']}) | {entry['description']} |"
        )
    return "\n".join(lines)


def render_section(section: dict, data: dict) -> str:
    parts = []
    heading = "#" * section["level"]
    parts.append(f"{heading} {section['title']}")

    if "description" in section:
        parts.append("")
        parts.append(section["description"])

    if section.get("key") and section["key"] in data:
        parts.append("")
        parts.append(render_table(data[section["key"]]))

    if "suffix" in section:
        parts.append(section["suffix"])

    if "children" in section:
        for child in section["children"]:
            parts.append("")
            parts.append(render_section(child, data))

    return "\n".join(parts)


def generate() -> str:
    root = Path(__file__).parent
    with open(root / "readme.json", encoding="utf-8") as f:
        data = json.load(f)

    parts = [HEADER, "---", build_toc(SECTIONS), "---"]

    for section in SECTIONS:
        parts.append(render_section(section, data))
        parts.append("---")

    parts.append(FOOTER)

    return "\n\n".join(parts) + "\n"


def generate_site() -> None:
    root = Path(__file__).parent
    with open(root / "readme.json", encoding="utf-8") as f:
        raw_json = f.read()
    docs_dir = root / "docs"
    docs_dir.mkdir(exist_ok=True)
    html = SITE_TEMPLATE.replace("{{ENTRIES_JSON}}", raw_json)
    site = docs_dir / "index.html"
    site.write_text(html, encoding="utf-8")
    print(f"Generated {site}")


if __name__ == "__main__":
    root = Path(__file__).parent
    readme = root / "README.md"
    content = generate()
    readme.write_text(content, encoding="utf-8")
    print(f"Generated {readme}")
    generate_site()
