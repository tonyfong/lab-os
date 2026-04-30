# LIMS Project Foundation — STORY-2 Specification

## Overview
Single HTML file that establishes the foundation for the LIMS prototype.
All other stories depend on this file.

## Contents

### 1. Role Selector
Dropdown to select one of four roles:
- **Brand Rep** — submits test orders
- **Lab Receptionist** — registers incoming samples
- **Lab Technician** — enters test results
- **Lab Director** — approves results and generates PDF report

### 2. Hardcoded Reference Data

#### Products (5)
| ID | Name | SKU | Category |
|----|------|-----|----------|
| P001 | Cotton T-Shirt | CT-2024-A | Apparel |
| P002 | Denim Jeans | DJ-2024-B | Apparel |
| P003 | Polyester Jacket | PJ-2024-C | Apparel |
| P004 | Cotton Fabric Roll | CFR-2024-R | Fabric |
| P005 | Wool Sweater | WS-2024-W | Apparel |

#### Tests (5) with Reference Ranges
| ID | Name | Unit | Normal Range | Method |
|----|------|------|--------------|--------|
| T001 | Colorfastness to Washing | Grade | ≥ 3.0 | ISO 105-C10 |
| T002 | Shrinkage | % | ≤ 5.0 | ISO 6330 |
| T003 | pH Value | pH | 4.5 – 8.5 | ISO 3071 |
| T004 | Tensile Strength | N | ≥ 200 | ISO 13934-2 |
| T005 | REACH Chemical (AZO) | mg/kg | ≤ 30 | ISO 14362 |

#### Demo Users (4)
| ID | Name | Role | Staff ID |
|----|------|------|----------|
| U001 | Sarah Chen | Brand Rep | BR-001 |
| U002 | John Lam | Lab Receptionist | LR-001 |
| U003 | Mary Wong | Lab Technician | LT-001 |
| U004 | Dr. Alan Ng | Lab Director | LD-001 |

### 3. UI Structure
- Header: "LIMS Prototype v0.1 — Textile Testing"
- Role selector (dropdown)
- Dynamic panel below that changes based on selected role
- For Story-2: just render a welcome card with selected role and display all reference data in a tabbed view

### 4. Acceptance Criteria
- [x] Single `index.html` file, no build step required
- [x] Role dropdown shows all 4 roles
- [x] Selecting a role updates the welcome message
- [x] All 5 products displayed in a table
- [x] All 5 tests with reference ranges displayed
- [x] All 4 demo users displayed
- [x] No external dependencies except CDN-hosted (jsPDF for future reports)
- [x] Clean, professional appearance suitable for lab environment

### 5. Technical
- Single file: `index.html` (inline CSS + JS)
- CDN: jsPDF (for future STORY-6 PDF generation)
- No local storage, no backend
- Color palette: clean whites/grays with blue accent (#2563EB)
