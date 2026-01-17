# Pawpal Hero – Crowdfunding Back End  
Monica Taccoli

## Planning

### Pawpal Hero  
**Be a Pet’s Saviour**

Pawpal Hero is a Django-based crowdfunding platform designed to prevent the euthanasia of dogs and cats by funding guaranteed, ethical care through a **time-based rescue model**. Instead of abstract fundraising goals, donations are converted into **measurable foster days**, ensuring each Pawpal is safe while awaiting a permanent home.

This project demonstrates how backend architecture can support **transparent, ethical, and human-centred outcomes** in animal welfare.

---

## The Twist: Foster-to-Save Milestone System

Each donation directly extends a Pawpal’s guaranteed care period:

- Every Pawpal has a daily cost representing food, shelter, veterinary care, staff wages, and facility costs.  
- Donations extend the Pawpal’s `funded_until` date.  
- Example: A $50 donation may fund 7 days of guaranteed safety.

> Every donation literally buys time for a Pawpal to live.

---

## Intended Audience / User Stories

### Intended Audience
- Animal lovers who want to help but cannot adopt  
- People interested in ethical, transparent crowdfunding  
- Community members seeking ongoing, measurable impact  
- Administrators managing animal welfare operations  

### User Stories
- As a donor, I want my donation to directly fund a Pawpal’s care time.  
- As a donor, I want to see how many foster days my donation secures.  
- As an admin, I want to manage Pawpal profiles and care costs accurately.  
- As an admin, I want to ensure funds are allocated fairly and transparently.

---

## Front End Pages / Functionality

### Home Page
- Displays branding and slogan *“Be a Pet’s Saviour”*  
- Explains the Foster-to-Save model  
- Shows total foster days funded across all Pawpals  
- Call-to-action to donate  

### Pawpals Page
- Lists all Pawpals currently seeking funding  
- Pawpal cards show:
  - Name, age, species  
  - Story and care needs  
  - Daily cost  
  - Funded days vs required days  
  - Visual progress bar  
  - Donate button to add safety days  

### Campaigns Page
- Displays transparent care campaigns:
  - Veterinary Care  
  - Food & Boarding  
  - Staff Wages  
  - **Forever Home Facility (Rent & Utilities)**  
- Shows funding targets and progress  
- Campaigns remain open after reaching their goal  

### Donation Page
- Accepts one-off donations  
- Shows how many foster days the donation unlocks  
- Confirms impact immediately (e.g. “You funded 7 days of safety”)  

### Admin Dashboard
- Manage Pawpal profiles and daily costs  
- Track foster milestones and funding timelines  
- Record expenses and campaign allocations  

---

## Key Platform Rules

### No Popularity Contest
Funding priority is based on **urgency (time remaining)**, not pet popularity.

### Overflow Funding Rule
Campaigns remain open after reaching their funding goal. Any surplus funds are automatically redirected to extend foster time for Pawpals with the least remaining safety time.

---

## API Spec (Minimal)

| URL | HTTP Method | Purpose | Request Body | Success Code | Authentication |
| --- | ----------- | ------- | ------------ | ------------ | -------------- |
| /api/pawpals/ | GET | List all Pawpals | None | 200 | Public |
| /api/pawpals/<id>/ | GET | Retrieve Pawpal details | None | 200 | Public |
| /api/donations/ | POST | Make donation → extend foster time | Donation object | 201 | Public |
| /api/campaigns/ | GET | View campaigns and progress | None | 200 | Public |

---

## Minimal Database Schema

Core Models:
- **Pawpal** (`name`, `daily_cost`, `funded_until`)  
- **Donation** (`donor`, `pawpal`, `amount`, `days_funded`)  
- **Campaign** (`name`, `target_amount`, `current_amount`)  
- **Expense** (vet care, food, wages, facility)

Funding logic is time-based, transparent, and auditable by design.

![Database Schema](./schema.png)
