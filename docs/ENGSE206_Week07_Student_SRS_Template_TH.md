# [System Name] — Software Requirements Specification Draft v1

## 0. Document Control

| Field | Value |
|---|---|
| Case ID | `[CASE-ID]` |
| Document ID | `[CASE-ID]-SRS-W07-v1` |
| Version | `0.1-draft` |
| Status | Draft / Baseline Candidate |
| Team/Owner | `[team]` |
| W05 source snapshot | `[artifact/version/hash]` |
| W06 source snapshot | `[artifact/version/hash]` |

## 1. Introduction

### 1.1 Purpose

`[กำหนดอะไร ใครใช้ และส่งต่อไปทำอะไร]`

### 1.2 Problem and Goals

| Goal | Desired outcome | Source | Status |
|---|---|---|---|
| `[G-xx]` | `[outcome]` | `[F/E/TD]` | Fact / Decision / Assumption |

### 1.3 Product Scope

| In Scope | Out of Scope / Extension | Reason/source |
|---|---|---|
| `[capability]` | `[item]` | `[why/source]` |

### 1.4 Definitions

| Term | Meaning | Source/Decision |
|---|---|---|
| `[term]` | `[business meaning]` | `[source]` |

## 2. Overall Description

### 2.1 Product Context

`[system boundary, system of record และ external systems โดยไม่เลือก technology]`

### 2.2 User Classes and Authority

| Actor | Goal | Authorized actions | Restrictions | Source |
|---|---|---|---|---|
| `[ACT-xx]` | `[goal]` | `[actions]` | `[limits]` | `[source]` |

### 2.3 Capabilities

| CAP | Capability | FR/BR/NFR/DR | US/UC/AC | Coverage |
|---|---|---|---|---|
| `[CAP-xx]` | `[name]` | `[IDs]` | `[IDs]` | Detailed / Partial |

### 2.4 Constraints and Assumptions

| ID | Type | Statement | Source | Status/next action |
|---|---|---|---|---|
| `[CT/AS-xx]` | Constraint / Assumption / TD | `[statement]` | `[source]` | `[status]` |

### 2.5 External Interfaces

| ID | System | Data/direction | Core/Extension | TBD/failure concern |
|---|---|---|---|---|
| `[EXT-xx]` | `[name]` | `[exchange]` | `[scope]` | `[unknown]` |

## 3. Functional Requirements

จัดกลุ่มตาม capability/workflow ทุก W05 FR ต้องมี disposition

| FR | Requirement | Source | Priority/admission | BR/NFR/DR | US/UC/AC | Status |
|---|---|---|---|---|---|---|
| `[FR-xx]` | `ระบบต้อง…` | `[F/E/TD]` | `[Must/Core]` | `[IDs]` | `[IDs]` | Ready / Partial / TBD |

### Detailed Requirement Record

| Field | Value |
|---|---|
| Requirement ID | `[FR-xx]` |
| Statement | `ระบบต้อง…` |
| Rationale/Goal | `[G-xx/why]` |
| Source | `[F/E/TD]` |
| Priority/Admission | `[Must/Should/Could] / [Core/Supporting/Extension]` |
| Trigger | `[observable event]` |
| Preconditions/guards | `[state/rule]` |
| Expected result | `[state/data/event]` |
| BR/NFR/DR links | `[IDs]` |
| US/UC/AC links | `[IDs]` |
| Verification | `[method + scenario]` |
| Status/TBD | `[status + gap/evidence need]` |

## 4. Business Rules

| BR | Rule | Authority/source | Affected FR/UC | Status |
|---|---|---|---|---|
| `[BR-xx]` | `[rule]` | `[TD/source]` | `[IDs]` | Confirmed for case / TBD |

## 5. Non-functional Requirements

| NFR | Quality statement | Context/stimulus | Response/measure | Source | Verification | Status/TBD |
|---|---|---|---|---|---|---|
| `[NFR-xx]` | `ระบบต้อง…` | `[context]` | `[measure or TBD]` | `[source]` | `[method]` | `[status]` |

## 6. Data Requirements

ส่วนนี้เป็น conceptual data requirement ยังไม่ใช่ physical database schema

| DR | Concept | Requirement/minimum data | Relationships | Classification | Source | Status |
|---|---|---|---|---|---|---|
| `[DR-xx]` | `[concept]` | `[meaning + minimum data]` | `[concept links]` | `[class]` | `[IDs]` | Ready / TBD |

## 7. Behavioral Model References

| Model | IDs/version | Requirement anchors | Coverage/gap | SRS use |
|---|---|---|---|---|
| User Stories | `[US-*]` | `[W05 IDs]` | `[coverage]` | `[section]` |
| Use Cases | `[UC-*]` | `[W05 IDs]` | `[level/gap]` | `[section]` |
| Acceptance Criteria | `[AC-*]` | `[W05 IDs]` | `[coverage]` | `[verification]` |

### 7.1 Lifecycle Rules

| From | Trigger | To | Guard/result | Source |
|---|---|---|---|---|
| `[state]` | `[event]` | `[state]` | `[guard]` | `[ID]` |

## 8. External Interface Requirements

| Interface | Requirement/data | Direction | Owner | Failure/privacy concern | Status |
|---|---|---|---|---|---|
| `[EXT-xx]` | `[what]` | `[in/out]` | `[owner]` | `[concern]` | Core / Extension / TBD |

## 9. Traceability and Coverage

| Source | W05 requirement | W06 model | SRS section | Verification | Coverage |
|---|---|---|---|---|---|
| `[F/E/TD]` | `[FR/BR/NFR/DR]` | `[US/UC/AC]` | `[หัวข้อ ]` | `[VF/method]` | Covered / Partial |

## 10. Open Issues

| OI | Question/TBD | Affected IDs | Owner | Next action | Expected evidence | Needed by |
|---|---|---|---|---|---|---|
| `[OI-xx]` | `[unknown]` | `[IDs]` | `[role]` | `[action]` | `[evidence]` | `[milestone]` |

## 11. Verification Plan

| VF | Method | Target IDs | Procedure/evidence | Owner | Status |
|---|---|---|---|---|---|
| `[VF-xx]` | Review / Demo / Test / Analysis / Inspection | `[IDs]` | `[how/evidence]` | `[owner]` | Planned |

## 12. Review Gate

- [ ] W05 FR/BR/NFR/DR ทุกข้อมี disposition
- [ ] W06 US/UC/AC ย้อนกลับ W05 ได้
- [ ] Partial/Extension/TBD มองเห็น
- [ ] Open Issue ทุกข้อมี owner/action/evidence
- [ ] Status ยังเป็น Baseline Candidate

## Appendix A — Requirement Disposition

| Backlog ID | Included/Deferred/Extension/Issue | SRS section | Reason |
|---|---|---|---|
| `[ID]` | `[disposition]` | `[หัวข้อ ]` | `[reason]` |

## Appendix B — Review and Revision

| Item | Before | After | Reason/source | Reviewer |
|---|---|---|---|---|
| `[ID/section]` | `[old]` | `[new]` | `[why]` | `[name]` |

## Appendix C — AI Use Disclosure

| Activity | AI assistance | Human verification/change | Evidence |
|---|---|---|---|
| `[task]` | `[what AI did]` | `[accepted/rejected/changed]` | `[path/link]` |
