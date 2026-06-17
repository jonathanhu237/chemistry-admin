## Purpose

Define the browser-based student H5 login behavior for the SYSU chemistry experiment learning platform.
## Requirements
### Requirement: Student H5 Login Page
The platform SHALL provide a student H5 login page at the backend root path and keep the admin console under `/admin`.

#### Scenario: Student login page is served
- **WHEN** a browser requests `/`
- **THEN** the backend MUST serve the student H5 application
- **AND** the admin console MUST remain available under `/admin`

#### Scenario: Student login uses student ID and password
- **WHEN** a student signs in from the H5 login page
- **THEN** the form MUST require only student ID and password
- **AND** it MUST call a student-scoped login endpoint instead of the admin login endpoint

### Requirement: Initial Password Activation
The backend SHALL treat first login with an accepted initial password as account activation and require a password change before the student can continue.

#### Scenario: First login activates a roster student
- **WHEN** a roster student logs in with their student ID and valid initial password
- **THEN** the backend MUST create or bind a student account for that roster entry
- **AND** the login response MUST identify the student account as requiring a password change

#### Scenario: Initial-password student changes password
- **WHEN** a logged-in student whose account requires a password change submits the current password and a valid new password
- **THEN** the backend MUST update the password, clear the password-change requirement, revoke previous student sessions, and return a fresh login token

### Requirement: Student Login Isolation
Student H5 authentication SHALL be isolated from the admin login flow and SHALL use student-scoped token storage on the frontend.

#### Scenario: Admin credentials are rejected by the student page
- **WHEN** the student H5 receives a login response for a non-student account
- **THEN** it MUST discard the token and keep the user on the student login flow

#### Scenario: Student with initial password is blocked from protected student APIs
- **WHEN** a student account still requires a password change
- **THEN** protected student API dependencies MUST reject the request until the student password endpoint clears the requirement

### Requirement: Student ID Uniqueness
The roster SHALL enforce a single active entry for a normalized student ID.

#### Scenario: Duplicate active roster entries are prevented
- **WHEN** roster entries are migrated or inserted
- **THEN** active entries MUST be unique by normalized student ID
- **AND** disabled roster entries MUST NOT block future active entries for the same normalized student ID

### Requirement: Student activation state consistency
The student H5 login flow SHALL present first-login activation, forced password change, normal login, and post-reset login as one consistent account lifecycle.

#### Scenario: Pending roster student first login
- **WHEN** a roster student who has not activated an account logs in with an accepted initial password
- **THEN** the backend MUST create or bind the student account
- **AND** the H5 app MUST route the student to the forced password-change screen before protected learning screens

#### Scenario: Reset student logs in
- **WHEN** an activated student whose password was reset by an admin logs in with the reset password
- **THEN** the H5 app MUST route the student to the forced password-change screen if the backend marks `must_change_password`
- **AND** the student MUST receive a fresh token after changing the password

#### Scenario: Disabled roster student cannot continue
- **WHEN** a disabled roster student attempts first login or uses an old token for protected student APIs
- **THEN** the backend MUST reject protected access according to student authentication and role rules
- **AND** the H5 app MUST return to the login flow with a clear student-facing error
