#!/usr/bin/env node
// check-hex.mjs — zero-dependency raw-hex-color scan for the sessions repo.
// Mirrors the harness token linter (ARCHITECTURE.md §9): hex color literals live
// ONLY in the harness's config/tokens.json. Generated files are exempt via the
// DO-NOT-EDIT header in their first three lines. Exit 1 on any hit.

import { readdirSync, readFileSync } from 'node:fs';
import { extname, join, relative, resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

const SCAN_EXTS = new Set(['.ts', '.js', '.mjs', '.svelte', '.css', '.py', '.yaml', '.yml']);
// 'docs' matches the harness linter's exclusion semantics (session dirs use
// singular 'doc/', which IS scanned).
const SKIP_DIRS = new Set(['node_modules', '.git', 'dist', '.svelte-kit', 'docs']);
const GENERATED_MARKER = 'GENERATED FROM config/tokens.json — DO NOT EDIT';

// #RGB, #RGBA, #RRGGBB, #RRGGBBAA — longest alternative first; \b rejects
// longer word-character runs (e.g. 5- or 7-digit sequences, "#define").
const HEX_RE = /#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b/g;

function* walk(dir) {
	for (const entry of readdirSync(dir, { withFileTypes: true })) {
		if (entry.isDirectory()) {
			if (!SKIP_DIRS.has(entry.name)) yield* walk(join(dir, entry.name));
		} else if (entry.isFile()) {
			const ext = extname(entry.name).toLowerCase();
			if (ext === '.md') continue;
			if (SCAN_EXTS.has(ext)) yield join(dir, entry.name);
		}
	}
}

let hits = 0;
let scanned = 0;

for (const file of walk(ROOT)) {
	const text = readFileSync(file, 'utf8');
	const lines = text.split(/\r?\n/);
	if (lines.slice(0, 3).some((line) => line.includes(GENERATED_MARKER))) continue;
	scanned += 1;
	for (let i = 0; i < lines.length; i += 1) {
		for (const match of lines[i].matchAll(HEX_RE)) {
			hits += 1;
			console.log(`${relative(ROOT, file)}:${i + 1}: ${match[0]}`);
		}
	}
}

if (hits > 0) {
	console.error(`check-hex: ${hits} raw hex literal(s) found. Use tokens (var(--...)) instead.`);
	process.exit(1);
}
console.log(`check-hex: clean (${scanned} files scanned)`);
