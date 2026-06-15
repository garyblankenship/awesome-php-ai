#!/usr/bin/env php
<?php
declare(strict_types=1);

/**
 * Generate README.md and docs/index.html from readme.json.
 */

const SECTIONS = [
    [
        'key' => 'llm_frameworks',
        'title' => 'LLM Frameworks',
        'level' => 2,
        'description' => 'Full-featured frameworks for building LLM-powered applications.',
        'in_toc' => true,
    ],
    [
        'key' => 'llm_clients_adapters',
        'title' => 'LLM Clients & Adapters',
        'level' => 2,
        'description' => 'Client libraries and provider integrations.',
        'in_toc' => true,
    ],
    [
        'key' => null,
        'title' => 'Natural Language Processing',
        'level' => 2,
        'in_toc' => true,
        'children' => [
            [
                'key' => 'structured_output',
                'title' => 'Structured Output & Validation',
                'level' => 3,
            ],
            [
                'key' => 'ai_agents_orchestration',
                'title' => 'AI Agents & Orchestration',
                'level' => 3,
            ],
            [
                'key' => 'mcp_agent_tooling',
                'title' => 'MCP & Agent Tooling',
                'level' => 3,
            ],
            [
                'key' => 'laravel_integrations',
                'title' => 'Laravel Integrations',
                'level' => 3,
            ],
            [
                'key' => 'symfony_integrations',
                'title' => 'Symfony Integrations',
                'level' => 3,
            ],
            [
                'key' => 'utilities_tools',
                'title' => 'Utilities & Tools',
                'level' => 3,
            ],
        ],
    ],
    [
        'key' => 'machine_learning',
        'title' => 'Machine Learning',
        'level' => 2,
        'in_toc' => true,
    ],
    [
        'key' => 'computer_vision',
        'title' => 'Computer Vision',
        'level' => 2,
        'in_toc' => true,
    ],
    [
        'key' => 'vector_storage_rag',
        'title' => 'Vector Storage & RAG',
        'level' => 2,
        'in_toc' => true,
    ],
    [
        'key' => 'command_line_tools',
        'title' => 'Command Line Tools',
        'level' => 2,
        'in_toc' => true,
    ],
    [
        'key' => 'video_processing',
        'title' => 'Video Processing',
        'level' => 2,
        'in_toc' => true,
    ],
    [
        'key' => 'api_clients',
        'title' => 'API Clients',
        'level' => 2,
        'in_toc' => true,
    ],
    [
        'key' => 'learning_resources',
        'title' => 'Learning Resources',
        'level' => 2,
        'in_toc' => true,
        'suffix' => "\n### Tutorials & Documentation\n\n- [Fun With OpenAI and Laravel](https://laracasts.com/series/fun-with-openai-and-laravel) - Laracasts series on OpenAI with PHP and Laravel.\n- [PHP-ML Tutorials](https://php-ml.readthedocs.io/en/latest/tutorials/) - Learn how to use PHP-ML for machine learning.\n- [Rubix ML Docs](https://docs.rubixml.com/) - Comprehensive documentation for Rubix ML.",
    ],
    [
        'key' => 'data_manipulation',
        'title' => 'Data Manipulation',
        'level' => 2,
        'in_toc' => false,
    ],
];

const HEADER = <<<'MARKDOWN'
# Awesome PHP AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome PHP libraries and tools for AI, Machine Learning, and Natural Language Processing.

Contributions welcome! Read the [contributing guidelines](#contributing) to get started.
MARKDOWN;

const FOOTER = <<<'MARKDOWN'
## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Add your library/tool to `readme.json`
3. Include `name`, `url`, `description`, `stars`, and `tags`
4. Run `php generate-readme.php`
5. Commit `readme.json`, `README.md`, and `docs/index.html`
6. Submit a pull request

Please ensure your submission is relevant to PHP and AI/ML/NLP.

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
MARKDOWN;

const TEMPLATE_DIR = 'templates';
const TEMPLATE_FILE = 'index.html';

const README_JSON = 'readme.json';
const README_FILE = 'README.md';
const DOCS_DIR = 'docs';
const SITE_FILE = 'index.html';

/**
 * @param list<array<string, mixed>> $sections
 */
function build_toc(array $sections): string
{
    $lines = [];
    foreach ($sections as $section) {
        if ($section['in_toc'] ?? false) {
            $lines[] = sprintf('- [%s](#%s)', $section['title'], section_anchor($section));
        }
    }

    return "## Table of Contents\n\n" . implode("\n", $lines);
}

/**
 * @param array<string, mixed> $section
 */
function section_anchor(array $section): string
{
    return strtolower(str_replace(['&', ' '], ['', '-'], (string) $section['title']));
}

/**
 * @param list<array{name: string, url: string, description: string}> $entries
 */
function render_table(array $entries): string
{
    $lines = [
        '| Repo | Description |',
        '|---------|-------------|',
    ];

    foreach ($entries as $entry) {
        $lines[] = sprintf('| [%s](%s) | %s |', $entry['name'], $entry['url'], $entry['description']);
    }

    return implode("\n", $lines);
}

/**
 * @param array<string, mixed> $section
 * @param array<string, mixed> $data
 */
function render_section(array $section, array $data): string
{
    $parts = [];
    $heading = str_repeat('#', (int) $section['level']);
    $parts[] = sprintf('%s %s', $heading, $section['title']);

    if (array_key_exists('description', $section)) {
        $parts[] = '';
        $parts[] = (string) $section['description'];
    }

    $key = $section['key'] ?? null;
    if (is_string($key) && array_key_exists($key, $data) && is_array($data[$key])) {
        $parts[] = '';
        $parts[] = render_table($data[$key]);
    }

    if (array_key_exists('suffix', $section)) {
        $parts[] = (string) $section['suffix'];
    }

    if (isset($section['children']) && is_array($section['children'])) {
        foreach ($section['children'] as $child) {
            $parts[] = '';
            $parts[] = render_section($child, $data);
        }
    }

    return implode("\n", $parts);
}

/**
 * @return array<string, mixed>
 */
function read_data(string $root): array
{
    $json = read_text($root . '/' . README_JSON);

    try {
        $data = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
    } catch (JsonException $exception) {
        throw new RuntimeException('Unable to decode ' . README_JSON . ': ' . $exception->getMessage(), 0, $exception);
    }
    if (!is_array($data)) {
        throw new RuntimeException(README_JSON . ' must contain a JSON object');
    }

    validate_data($data);

    return $data;
}

/**
 * @param array<string, mixed> $data
 */
function validate_data(array $data): void
{
    $seenNames = [];
    $seenUrls = [];
    $knownSections = [];

    foreach (SECTIONS as $section) {
        collect_section_keys($section, $knownSections);
        validate_section_data($section, $data, $seenNames, $seenUrls);
    }

    foreach (array_keys($data) as $key) {
        if (!isset($knownSections[$key])) {
            throw new RuntimeException(sprintf('%s contains unknown section "%s"', README_JSON, $key));
        }
    }
}

/**
 * @param array<string, mixed> $section
 * @param array<string, true> $knownSections
 */
function collect_section_keys(array $section, array &$knownSections): void
{
    $key = $section['key'] ?? null;
    if (is_string($key)) {
        $knownSections[$key] = true;
    }

    if (isset($section['children']) && is_array($section['children'])) {
        foreach ($section['children'] as $child) {
            if (!is_array($child)) {
                throw new RuntimeException(sprintf('Section "%s" contains an invalid child section', $section['title']));
            }
            collect_section_keys($child, $knownSections);
        }
    }
}

/**
 * @param array<string, mixed> $section
 * @param array<string, mixed> $data
 * @param array<string, string> $seenNames
 * @param array<string, string> $seenUrls
 */
function validate_section_data(array $section, array $data, array &$seenNames, array &$seenUrls): void
{
    $key = $section['key'] ?? null;
    if (is_string($key)) {
        if (!array_key_exists($key, $data)) {
            throw new RuntimeException(sprintf('%s is missing section "%s"', README_JSON, $key));
        }
        if (!is_array($data[$key])) {
            throw new RuntimeException(sprintf('Section "%s" must be an array', $key));
        }
        validate_entries($key, $data[$key], $seenNames, $seenUrls);
    }

    if (isset($section['children']) && is_array($section['children'])) {
        foreach ($section['children'] as $child) {
            if (!is_array($child)) {
                throw new RuntimeException(sprintf('Section "%s" contains an invalid child section', $section['title']));
            }
            validate_section_data($child, $data, $seenNames, $seenUrls);
        }
    }
}

/**
 * @param list<mixed> $entries
 * @param array<string, string> $seenNames
 * @param array<string, string> $seenUrls
 */
function validate_entries(string $sectionKey, array $entries, array &$seenNames, array &$seenUrls): void
{
    foreach ($entries as $index => $entry) {
        if (!is_array($entry)) {
            throw new RuntimeException(sprintf('Entry %d in "%s" must be an object', $index, $sectionKey));
        }

        foreach (['name', 'url', 'description'] as $field) {
            if (!isset($entry[$field]) || !is_string($entry[$field]) || $entry[$field] === '') {
                throw new RuntimeException(sprintf('Entry %d in "%s" must have a non-empty string "%s"', $index, $sectionKey, $field));
            }
        }

        validate_unique_entry($sectionKey, $index, $entry, $seenNames, $seenUrls);

        if (isset($entry['stars']) && (!is_int($entry['stars']) || $entry['stars'] < 0)) {
            throw new RuntimeException(sprintf('Entry %d in "%s" must have a non-negative integer "stars"', $index, $sectionKey));
        }

        if (isset($entry['tags'])) {
            if (!is_array($entry['tags'])) {
                throw new RuntimeException(sprintf('Entry %d in "%s" must have an array "tags"', $index, $sectionKey));
            }
            foreach ($entry['tags'] as $tag) {
                if (!is_string($tag) || $tag === '') {
                    throw new RuntimeException(sprintf('Entry %d in "%s" has an invalid tag', $index, $sectionKey));
                }
            }
        }
    }
}

/**
 * @param array<string, mixed> $entry
 * @param array<string, string> $seenNames
 * @param array<string, string> $seenUrls
 */
function validate_unique_entry(string $sectionKey, int $index, array $entry, array &$seenNames, array &$seenUrls): void
{
    $location = sprintf('%s[%d]', $sectionKey, $index);
    $nameKey = strtolower(trim((string) $entry['name']));
    $urlKey = strtolower(rtrim(trim((string) $entry['url']), '/'));

    if (isset($seenNames[$nameKey])) {
        throw new RuntimeException(sprintf('Duplicate entry name "%s" in %s; first seen in %s', $entry['name'], $location, $seenNames[$nameKey]));
    }
    if (isset($seenUrls[$urlKey])) {
        throw new RuntimeException(sprintf('Duplicate entry URL "%s" in %s; first seen in %s', $entry['url'], $location, $seenUrls[$urlKey]));
    }

    $seenNames[$nameKey] = $location;
    $seenUrls[$urlKey] = $location;
}

function generate_readme(string $root): string
{
    $data = read_data($root);
    $parts = [HEADER, '---', build_toc(SECTIONS), '---'];

    foreach (SECTIONS as $section) {
        $parts[] = render_section($section, $data);
        $parts[] = '---';
    }

    $parts[] = FOOTER;

    return implode("\n\n", $parts) . "\n";
}

function generate_site(string $root): void
{
    $data = read_data($root);
    $entriesJson = json_encode(
        $data,
        JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT
    );
    if ($entriesJson === false) {
        throw new RuntimeException('Unable to encode site data: ' . json_last_error_msg());
    }
    $template = read_site_template($root);

    $docsDir = $root . '/' . DOCS_DIR;
    if (!is_dir($docsDir) && !mkdir($docsDir, 0777, true) && !is_dir($docsDir)) {
        throw new RuntimeException('Unable to create docs directory');
    }

    $site = $docsDir . '/' . SITE_FILE;
    $html = str_replace('{{ENTRIES_JSON}}', $entriesJson, $template);
    if ($html === '' || substr($html, -1) !== "\n") {
        $html .= "\n";
    }
    write_text($site, $html);

    echo 'Generated ' . $site . PHP_EOL;
}

function read_site_template(string $root): string
{
    $template = read_text($root . '/' . TEMPLATE_DIR . '/' . TEMPLATE_FILE);
    if (!str_contains($template, '{{ENTRIES_JSON}}')) {
        throw new RuntimeException(sprintf('%s/%s is missing {{ENTRIES_JSON}} placeholder', TEMPLATE_DIR, TEMPLATE_FILE));
    }

    return $template;
}

function read_text(string $path): string
{
    $contents = file_get_contents($path);
    if ($contents === false) {
        throw new RuntimeException('Unable to read ' . $path);
    }

    return $contents;
}

function write_text(string $path, string $contents): void
{
    if (file_put_contents($path, $contents) === false) {
        throw new RuntimeException('Unable to write ' . $path);
    }
}

function main(): int
{
    $root = __DIR__;
    $readme = $root . '/' . README_FILE;
    write_text($readme, generate_readme($root));

    echo 'Generated ' . $readme . PHP_EOL;
    generate_site($root);

    return 0;
}

try {
    exit(main());
} catch (Throwable $throwable) {
    fwrite(STDERR, 'Error: ' . $throwable->getMessage() . PHP_EOL);
    exit(1);
}
