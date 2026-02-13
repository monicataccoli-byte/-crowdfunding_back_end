# Crowdfunding Back End
Monica Taccoli

## Planning:

This project was planned as a **backend-first Django REST application** focusing on ethical crowdfunding logic, clear data modelling, and transparent financial tracking.

The core design principle was to replace popularity-based fundraising with a **time-based rescue model**, ensuring fairness and dignity for every animal listed. The system was intentionally scoped to:

- Demonstrate strong REST API design
- Apply relational database modelling using SQLite
- Implement meaningful business logic (money → foster days)
- Prevent overfunding and ensure accountability
- Remain realistic and achievable within a portfolio timeframe

The planning phase prioritised:
- Clear separation of concerns (models, serializers, views)
- REST-aligned endpoint naming
- Transparent donation tracking
- Admin-controlled data integrity

---

### Concept/Name

**Pawse Furever** is a Django-based crowdfunding platform built to prevent the euthanasia of dogs and cats by funding guaranteed, ethical care through a **time-based rescue model**.

Each animal is listed as a **Pawse Furlife**. Instead of raising abstract fundraising totals, donations are converted into measurable **foster days**, extending a Pawse Furlife’s `funded_until` date. This ensures the animal remains safe while awaiting adoption or lifelong sanctuary care.

The project focuses on backend architecture, ethical business logic, and transparent financial tracking using Django REST Framework and SQLite.

---

### Intended Audience/User Stories

#### Intended Audience
- Animal lovers who want to contribute but cannot adopt
- Donors seeking transparency and measurable impact
- Shelter administrators managing animals at risk
- Community members supporting ethical rescue programs

#### User Stories

- As a donor, I want to donate money so I can help prevent euthanasia.
- As a donor, I want my donation converted into funded days so I can clearly see my impact.
- As a donor, I want to sponsor a specific Pawse Furlife so I can form an emotional connection.
- As a donor, I want transparency about how funds are used (care, wages, rent, vet bills).
- As an admin, I want to create and update Pawse Furlife profiles so records remain accurate.
- As an admin, I want to track campaign funds and expenses to ensure accountability.

---

### Front End Pages/Functionality

- **Home Page**
    - Displays the slogan *“Be a Pet’s Saviour”*
    - Explains the time-based Foster-to-Save model
    - Shows total foster days funded across the platform
    - Provides clear donation call-to-action buttons

- **Pawse Furlife Listing Page**
    - Displays all Pawse Furlife profiles
    - Shows urgency status
    - Displays funded-until date
    - Links to detailed Pawse Furlife pages

- **Pawse Furlife Detail Page**
    - Shows name, age, species, and story
    - Displays daily care cost
    - Displays remaining funded days
    - Allows users to donate directly

- **fundraiser Page**
    - Lists active campaigns (Vet Fund, Staffing Fund, Facilities Fund)
    - Displays funding targets and progress
    - Redirects excess support to urgent Pawse Furlife cases

- **Admin Dashboard**
    - Create, update, or delete Pawse Furlife profiles
    - Create and manage campaigns
    - Record expenses (vet care, wages, rent, food)
    - View donation reports

---

### API Spec

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
| /api/fundraiser/ | GET | Retrieve all fundraisers | None | 200 OK | Public |
| /api/fundraiser/ | POST | Create fundraisers | funrdraisers JSON | 201 Created | Admin |
| /api/fundraiser/{id}/ | GET | Retrieve fundraisers details | None | 200 OK | Public |
| /api/pledges/ | POST | Create a donation/pledge | Pledge JSON | 201 Created | Authenticated |

> Business logic converts pledge amounts into foster days and extends the Pawse Furlife `funded_until` date.

---

### DB Schema

The database schema includes relational models for:

- PawseFurlife
- Fundraiser
- Pledge
- Expense
- User (Django built-in)

SQLite is used for development and portfolio demonstration due to its simplicity, zero configuration, and suitability for small-to-medium scale applications.

![](./relative/path/to/your/schema/image.png)
