# efflow 

Manage and process "flows" with associated tags using a PostgreSQL backend.

## Quick Setup

1. **Clone**: `git clone <repository_url>`
2. **Run with Docker**: Navigate to the project root and execute `docker-compose up --build`.

## Design Highlights

- Tables: `Flows`, `Tags`, and `FlowTags` (association table).
- Timestamps `created_at` and `updated_at` in both `Flows` and `Tags`.

## Troubleshooting

Check Docker logs for errors: `docker-compose logs <service_name>`.

Ensure database configurations and credentials are consistent.
