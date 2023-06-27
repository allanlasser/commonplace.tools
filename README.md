# commonplace.tools
Decentralized Tool Share

## Development

We user Docker to package up our application into deterministic runtimes.

### Backend

The backend uses Django with DRF. It's also fun and nice.

To serve the backend with Docker:

```
docker compose up backend-local
```

### Frontend

To serve the frontend with Docker:

```
docker compose up frontend-local
```

To run the frontend on your machine:

```sh
cd frontend
npm install
# if you're running locally:
npm run dev -- --open
# if you're using Codespaces:
npm run dev -- --host
```

If you're using Codespaces, using `--host` exposes the port to the network.

## Production

To run the production stack:

```
docker compose up backend frontend
```
