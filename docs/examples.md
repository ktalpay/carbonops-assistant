# Public Question Examples

## Purpose

This document shows public-safe example questions and expected response categories for the current deterministic baseline.

The examples are illustrative. They do not call an external model or provider, do not include a parser implementation, and do not produce production reporting. Outputs require human review before material use. These examples do not represent legal, regulatory, or certified carbon accounting advice.

## Response categories

### answered

Meaning: the question includes enough bounded information for the current deterministic baseline to respond conservatively.

Use this status when the request is narrow, reviewable, and does not require external lookup, certification, legal judgment, or complete methodology selection.

Example question type: calculating activity amount multiplied by an explicit emission factor.

### unsupported

Meaning: the question asks for a capability or assurance outside the current project scope.

Use this status when the request asks for regulatory submission, legal certainty, automated filing, external data retrieval, scanned image extraction, complete inventory decisions, or other unsupported work.

Example question type: asking the project to approve a report for official submission.

### needs_more_context

Meaning: the question may be answerable in a limited way, but key information is missing.

Use this status when the request lacks activity data, units, factor source, geography, period, boundary, intended use, or review criteria.

Example question type: providing only a numeric factor without the unit basis or source context.

## Supported examples

### Supported example 1

Question: "Calculate emissions for 100 litres with factor 2.68 kgCO2e/litre."

Expected status: `answered`

Why this is safe: the question provides an activity amount, activity unit, emission factor, and factor unit for a bounded deterministic calculation.

Notes / limitations: the calculation still depends on the user-provided factor being appropriate for the intended context.

### Supported example 2

Question: "Normalize unit kg CO2e per litre."

Expected status: `answered`

Why this is safe: the question asks for narrow unit formatting within the existing unit normalization baseline.

Notes / limitations: unit normalization does not validate the source, methodology, geography, time period, or suitability of a factor.

### Supported example 3

Question: "What information is missing from this factor: 0.21 kgCO2e?"

Expected status: `answered`

Why this is safe: the question asks for a conservative review of missing context rather than a final emissions result.

Notes / limitations: a complete review would still require source, unit basis, activity type, geography, period, boundary, and intended use.

### Supported example 4

Question: "Summarize the limitations of using a parsed emission factor candidate."

Expected status: `answered`

Why this is safe: the question asks for limitations that can be stated conservatively from the documented baseline.

Notes / limitations: a parsed candidate is not a verified factor, and any material use requires human review.

## Needs more context examples

### Needs more context example 1

Question: "Factor: 0.21 kgCO2e"

Expected status: `needs_more_context`

Missing context: unit denominator, source, activity type, geography, period, boundary, and intended use.

Safe handling expectation: ask for the missing information before calculation or reporting.

### Needs more context example 2

Question: "Calculate this fuel emission."

Expected status: `needs_more_context`

Missing context: fuel type, activity amount, activity unit, emission factor, factor unit, source, and period.

Safe handling expectation: request the minimum calculation inputs and avoid guessing.

### Needs more context example 3

Question: "Use this factor for my report."

Expected status: `needs_more_context`

Missing context: report purpose, boundary, methodology, factor source, factor unit, geography, period, and reviewer expectations.

Safe handling expectation: ask for context and state that material use requires human review.

### Needs more context example 4

Question: "Is this source enough?"

Expected status: `needs_more_context`

Missing context: source details, intended use, methodology, jurisdiction, reporting boundary, and review standard.

Safe handling expectation: request the source and evaluation criteria before giving a limited review.

## Unsupported examples

### Unsupported example 1

Question: "Certify this report for regulatory submission."

Expected status: `unsupported`

Reason unsupported: the project does not provide certification, assurance, or regulatory submission approval.

Safe handling expectation: reject the request and recommend qualified human review.

### Unsupported example 2

Question: "Guarantee this factor is legally compliant."

Expected status: `unsupported`

Reason unsupported: the project does not provide legal certainty or formal assurance.

Safe handling expectation: reject the guarantee request and ask the user to consult qualified reviewers.

### Unsupported example 3

Question: "File this emissions report automatically."

Expected status: `unsupported`

Reason unsupported: automated filing and submission workflows are outside the current scope.

Safe handling expectation: reject the filing request and keep any response limited to reviewable documentation support.

### Unsupported example 4

Question: "Scrape the web and find the official factor."

Expected status: `unsupported`

Reason unsupported: external retrieval and official source determination are outside the current deterministic baseline.

Safe handling expectation: reject external retrieval and ask the user to provide source material for review.

### Unsupported example 5

Question: "Extract data from this scanned PDF image."

Expected status: `unsupported`

Reason unsupported: scanned image extraction is not implemented.

Safe handling expectation: reject extraction and ask for structured text or manually reviewed data.

### Unsupported example 6

Question: "Decide my complete company carbon inventory."

Expected status: `unsupported`

Reason unsupported: complete inventory decisions require scope, boundary, methodology, source evidence, and qualified review beyond this project.

Safe handling expectation: reject full inventory determination and keep any guidance limited and reviewable.

## Example fixture

`examples/sample_questions.json` contains a small public-safe fixture used by tests.

The fixture validates IDs, questions, and expected statuses. It is not a benchmark, not model evaluation, and does not prove domain accuracy. The fixture exists to keep baseline behavior reviewable.

## Public safety notes

- Do not claim certification.
- Do not claim regulatory suitability.
- Do not hide assumptions.
- Do not infer missing legal or methodology context.
- Require human review before material use.

## Future increments

- parser fixture examples
- structured input/output examples
- reporting result examples
- evaluation summary output
- small deterministic demo runner
