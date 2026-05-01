# Source Metadata Model

## Purpose

Source metadata provides context around extracted emission factor candidates.

Source metadata is not proof of correctness. It is not validation by itself. It helps human reviewers understand where a candidate came from, what context was available, and what context was missing.

This is a documentation contract only. No parser, crawler, or extraction implementation is included.

## Scope

In scope:

- source title
- source URL
- source organization
- published date
- retrieved date
- source section or page reference
- input record identifier
- extraction note
- reviewer note
- metadata completeness warnings

Out of scope:

- automated web lookup
- web crawling
- PDF extraction
- OCR
- source credibility scoring
- legal or regulatory interpretation
- compliance approval
- production reporting

## Metadata fields

The future source metadata object is conceptual and uses these fields.

| Field | Type | Required? | Description |
| --- | --- | --- | --- |
| `sourceId` | string | Yes | Stable identifier for the source record within a local dataset. |
| `inputId` | string | Yes | Identifier that connects source metadata to parser input. |
| `sourceTitle` | string | No | Title or short label for the source. |
| `sourceUrl` | string | No | URL for the source, when present. This is not proof of correctness. |
| `sourceOrganization` | string | No | Organization named by the source metadata, when present. |
| `sourcePublishedAt` | string | No | Publication date or version date, when present. |
| `sourceRetrievedAt` | string | No | Retrieval date, when present. This is contextual only. |
| `sourceSection` | string | No | Section, heading, table label, or local reference within the source. |
| `sourcePage` | string or number | No | Page reference, when available. |
| `sourceLicense` | string | No | License or reuse note, when available. |
| `sourceNotes` | string | No | Human-readable notes about the source context. |
| `extractionNotes` | string | No | Notes about how the candidate text was identified. |
| `reviewerNotes` | string | No | Notes added during human review. |
| `metadataWarnings` | list of strings | Yes | Warning categories for missing or incomplete metadata. |

`sourceId` should be stable within a local dataset. `inputId` connects source metadata to parser input. `sourceUrl` may be absent, and a present `sourceUrl` is not proof of correctness. Retrieved date is contextual only. `metadataWarnings` should not be hidden.

## Metadata completeness levels

| Level | Meaning | Expected handling |
| --- | --- | --- |
| `complete` | Core source title, organization, URL or local reference, and date context are present. | Preserve metadata and still require normal validation and human review. |
| `partial` | Some useful context is present, but one or more core fields are missing. | Candidate extraction may proceed if limitations and warnings are explicit. |
| `minimal` | Only a small amount of source context is present. | Treat as weak context and surface warnings prominently. |
| `missing` | No useful source context is available. | Trigger warnings or `needs_more_context` where source context is material. |

Complete metadata still does not prove factor correctness. Missing metadata should trigger warnings or `needs_more_context`. Partial metadata can still support candidate extraction if limitations are explicit.

## Warning categories

- `missing_source_title`: no title or source label is available.
- `missing_source_url`: no URL is available.
- `missing_source_organization`: no organization is identified.
- `missing_published_date`: no publication or version date is available.
- `missing_retrieved_date`: no retrieval date is available.
- `ambiguous_source`: the source identity is unclear or mixed with another source.
- `source_context_incomplete`: important source context is absent.
- `source_license_unknown`: reuse or license context is not available.
- `source_not_publicly_reviewable`: the source cannot be reviewed from public or local context.

## Relationship with parser contract

Parser input may include source metadata fields. Parser output may copy selected source metadata fields or source references. Metadata warnings should appear in parser output warnings.

Metadata does not override parser validation. Missing metadata may lead to `needs_more_context` when source context is needed for safe interpretation.

## Relationship with validation

Source metadata helps reviewers inspect context. Numeric parsing and unit normalization are separate checks. Source metadata alone does not validate an emission factor.

Conflicts between source metadata and extracted text should be surfaced as warnings instead of silently resolved.

## Relationship with reporting result contract

Future reporting outputs may include source metadata references. Reporting outputs should separate calculated values from source notes. Source metadata should not imply legal or regulatory acceptance.

Reporting results may include source references and metadata warnings. Source metadata improves traceability, but it does not imply regulatory acceptance or correctness.

## Example metadata records

### Complete metadata

```text
sourceId: source-001
inputId: input-001
sourceTitle: Example public factor table
sourceUrl: https://example.org/factors
sourceOrganization: Example Organization
sourcePublishedAt: 2025-01-15
sourceRetrievedAt: 2026-05-01
sourceSection: Table 2
metadataWarnings: []
```

### Partial metadata

```text
sourceId: source-002
inputId: input-002
sourceTitle: Example fuel factor note
sourceOrganization: Example Organization
metadataWarnings: [missing_source_url, missing_published_date, missing_retrieved_date]
```

### Missing metadata

```text
sourceId: source-003
inputId: input-003
metadataWarnings: [missing_source_title, missing_source_organization, source_context_incomplete]
```

## Public safety notes

- Do not imply source endorsement.
- Do not claim source correctness.
- Do not claim regulatory suitability.
- Do not hide missing metadata.
- Require human review for material use.

## Future implementation notes

Future increments may add:

- typed metadata object
- source metadata tests
- parser integration
- reporting contract integration
- example fixture validation

No code is added by this document.
