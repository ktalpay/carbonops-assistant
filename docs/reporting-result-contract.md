# Reporting Result Contract

## Purpose

This document defines a future reporting result contract for presenting calculated emissions-related outputs in a structured and reviewable format.

This is a documentation contract only. No reporting implementation is included. Calculated outputs require validation and human review. This is not a regulatory report, legal submission, or certification artifact.

The contract separates values, source notes, assumptions, warnings, and review status.

## Scope

In scope:

- calculation result identifiers
- activity amount
- activity unit
- emission factor value
- emission factor unit
- calculated emissions value
- calculated emissions unit
- source references
- assumptions
- warnings
- unsupported reasons
- review status
- calculation notes

Out of scope:

- automated regulatory submission
- legal interpretation
- complete carbon inventory reporting
- production reporting workflow
- PDF or spreadsheet report rendering
- third-party assurance
- provider integrations
- full methodology selection

## Result status model

| Status | Meaning | Typical use |
| --- | --- | --- |
| `calculated` | Arithmetic was performed with the supplied activity amount and emission factor. | Deterministic calculation where required numeric inputs are present. |
| `needs_more_context` | More context is needed before a safe reporting result can be produced. | Missing activity context, source references, units, or assumptions. |
| `unsupported` | A calculated result should not be produced. | Unsupported use, missing core inputs, or unsafe request. |
| `review_required` | A structured output is available but should not be used without human review. | Ambiguous inputs, incomplete metadata, or assumptions that need confirmation. |

`calculated` means arithmetic was performed, not that the result is certified or final. `review_required` means the output is structurally available but should not be used without human review. `unsupported` means the system should not produce a calculated result.

## Implemented model baseline

The current implementation includes a minimal `ReportingResult` dataclass with result status, input references, calculation fields, warnings, unsupported reasons, assumptions, and review status.

The model can serialize to a JSON-friendly dictionary. Decimal values are represented as strings, and warning, unsupported reason, and assumption fields are represented as lists.

This is a structural result model only. It does not render production reports, create filings, validate source credibility, or replace human review.

## Reporting result fields

The future reporting result object is conceptual and uses these fields.

| Field | Type | Required? | Description |
| --- | --- | --- | --- |
| `resultId` | string | Yes | Stable identifier for the reporting result. |
| `inputId` | string | Yes | Identifier for the input record or calculation request. |
| `resultStatus` | string | Yes | One of `calculated`, `needs_more_context`, `unsupported`, or `review_required`. |
| `activityLabel` | string | No | Activity, fuel, material, process, or category label. |
| `activityAmount` | string or number | No | Activity amount used in the calculation. |
| `activityUnit` | string | No | Activity unit as supplied. |
| `normalizedActivityUnit` | string | No | Normalized activity unit, when available. |
| `emissionFactorValue` | string or number | No | Emission factor value used in the calculation. |
| `emissionFactorUnit` | string | No | Emission factor unit as supplied or extracted. |
| `normalizedEmissionFactorUnit` | string | No | Normalized emission factor unit, when available. |
| `calculatedEmissionsValue` | string or number | No | Calculated emissions value, when arithmetic is supported. |
| `calculatedEmissionsUnit` | string | No | Unit for the calculated emissions value. |
| `sourceReferences` | list of objects | Yes | Source references linked to source metadata when available. |
| `assumptions` | list of strings | Yes | Explicit assumptions used for the result. |
| `warnings` | list of strings | Yes | Warning categories that must remain visible. |
| `unsupportedReasons` | list of strings | Yes | Reasons no supported reporting result can be produced. |
| `calculationNotes` | list of strings | Yes | Human-readable notes about the calculation. |
| `reviewStatus` | string | Yes | One of `not_reviewed`, `needs_review`, `reviewed`, or `rejected`. |
| `createdAt` | string | No | Local creation timestamp or date string, when available. |

`sourceReferences` should link to source metadata where available. Warnings must not be hidden. Assumptions must be explicit. Calculated values should not be presented as certified results.

## Source reference model

Reporting results may reference source metadata through compact source reference objects.

Conceptual source reference fields:

- `sourceId`
- `sourceTitle`
- `sourceUrl`
- `sourceOrganization`
- `sourcePublishedAt`
- `sourceRetrievedAt`
- `sourceSection`
- `sourcePage`
- `sourceWarnings`

Source references provide traceability, not proof of correctness. Missing source metadata should surface warnings. Source URLs should not be treated as validation.

## Warning categories

- `missing_source_reference`: no source reference is attached to the result.
- `missing_activity_context`: activity context is absent or unclear.
- `unsupported_unit`: a required unit is not recognized.
- `normalization_not_available`: unit normalization could not be performed.
- `assumption_required`: the result depends on an explicit assumption.
- `review_required`: human review is needed before material use.
- `incomplete_metadata`: source metadata is incomplete.
- `calculation_input_incomplete`: required calculation input is missing.
- `unsupported_reporting_use`: requested use is outside the supported scope.

## Review status

| Review status | Meaning | Notes |
| --- | --- | --- |
| `not_reviewed` | No human review has been recorded. | Default for newly created conceptual results. |
| `needs_review` | Human review is expected before use. | Useful when warnings or assumptions are present. |
| `reviewed` | A human reviewer has reviewed the result. | Workflow marker only, not legal assurance. |
| `rejected` | A human reviewer decided the result should not be used. | Keep rejection notes separate from calculated values. |

Review status should be separate from calculation status.

## Example reporting results

### Calculated result with source reference

```text
resultId: result-001
inputId: input-001
resultStatus: calculated
activityLabel: diesel combustion
activityAmount: 100
activityUnit: litre
emissionFactorValue: 2.68
emissionFactorUnit: kgCO2e/litre
calculatedEmissionsValue: 268
calculatedEmissionsUnit: kgCO2e
sourceReferences: [{sourceId: source-001, sourceTitle: Example public factor table}]
warnings: []
reviewStatus: needs_review
```

### Needs more context

```text
resultId: result-002
inputId: input-002
resultStatus: needs_more_context
warnings: [missing_activity_context, missing_source_reference]
unsupportedReasons: []
reviewStatus: needs_review
```

### Unsupported reporting use

```text
resultId: result-003
inputId: input-003
resultStatus: unsupported
warnings: []
unsupportedReasons: [unsupported_reporting_use]
reviewStatus: rejected
```

## Relationship with emissions helpers

Emissions helpers perform deterministic arithmetic. The arithmetic result is only one part of reporting output.

A reporting result also needs source references, assumptions, warnings, and review status. Arithmetic success does not imply reporting suitability.

## Relationship with parser contract

Parser output may provide factor candidates. Reporting results may consume parsed candidates only after validation. Parser warnings should carry forward into reporting warnings. Unsupported parser output should not produce calculated reporting results.

## Relationship with source metadata model

Reporting output may include source references. Source metadata improves traceability but does not prove correctness. Missing or partial source metadata should produce warnings.

## Public safety notes

- Do not claim certified accuracy.
- Do not claim regulatory suitability.
- Do not hide assumptions.
- Do not hide missing source metadata.
- Do not produce filing-ready claims.
- Require human review before material use.

## Future implementation notes

Future increments may add:

- example fixtures
- CSV or table reporting examples
- simple Markdown summary rendering
- validation summary output

Current code implements only the minimal structural model described above.
