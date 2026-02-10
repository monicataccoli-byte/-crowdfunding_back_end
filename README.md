# Pawse Furlife – Crowdfunding Back End  
Monica Taccoli

## Planning:

Pawse Furlife was planned as a backend-first Django REST application, focusing on **ethical crowdfunding for pets at risk of euthanasia**. The core twist is the **Time-Based Impact / Foster Days Tracker**, where each donation directly contributes to measurable foster days for a pet. This ensures transparency and allows donors to see the tangible impact of their contributions.

The planning process focused on:

1. **Defining the core concept** – Donations = foster days, tracked per pet.
2. **Identifying stakeholders** – Donors, foster carers, and admins.
3. **User stories and intended audience** – Ensure functionality meets real user needs.
4. **Model design** – Simple models: `Fundraiser`, `Pledge`, `User`.
5. **API endpoints** – Minimal RESTful routes: list fundraisers, view fundraiser details, make pledges.
6. **Simplification** – Removed surplus allocation and advanced features for clarity and faster implementation.

This structure ensures the project is **ethical, transparent, and easy to extend** in the future.

### Concept/Name
**Pawse Furlife** is a Django REST backend project designed to allow donors to fund measurable foster days for pets. Each donation extends the pet's foster care duration, tracked via the `funded_until` field.

### Intended Audience/User Stories
**Intended Audience:**  
- Animal lovers who want to make a real impact.  
- Foster carers managing pets in temporary care.  
- Administrators overseeing campaigns.

**User Stories:**  
- As a donor, I want my donation to directly contribute to a pet's foster days.  
- As a foster carer, I want to see how long pets can stay in care based on funding.  
- As an admin, I want to monitor fundraisers and pledges.

### Front End Pages/Functionality
- **Home / Fundraisers Listing Page**
    - Display all active campaigns.
    - Search and filter campaigns by pet type or urgency.
    - Click to view fundraiser details.
- **Fundraiser Detail Page**
    - Show pet info and foster day progress.
    - Allow donors to make pledges.
- **Admin Dashboard** (optional via Django Admin)
    - Manage fundraisers and pledges.
    - Monitor overall donations and foster days.

### Features
- Donations mapped to measurable foster days.  
- Track `funded_until` to show pet care duration.  
- Minimal, clean backend design for portfolio purposes.  
- Transparent and ethical crowdfunding logic.  



