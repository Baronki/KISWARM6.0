# KISWARM v6.0 Architecture

## Overview

KISWARM v6.0 is an integration platform combining:
- **KISWARM5.0 Backend** - 57 Python modules for AI swarm intelligence
- **kinfp-portal Frontend** - React/TypeScript banking portal
- **KIBank Modules** - New banking, investment, and reputation modules

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            KISWARM v6.0                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        FRONTEND LAYER                                │   │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐ │   │
│  │  │   React 18      │  │   TypeScript    │  │   Tailwind CSS      │ │   │
│  │  │   Components    │  │   Type Safety   │  │   shadcn/ui         │ │   │
│  │  └────────┬────────┘  └────────┬────────┘  └──────────┬──────────┘ │   │
│  │           │                    │                      │            │   │
│  │           └────────────────────┼──────────────────────┘            │   │
│  │                                │                                   │   │
│  │                     ┌──────────▼──────────┐                        │   │
│  │                     │   tRPC Client       │                        │   │
│  │                     │   Type-safe API     │                        │   │
│  │                     └──────────┬──────────┘                        │   │
│  └────────────────────────────────┼────────────────────────────────────┘   │
│                                   │                                        │
│  ┌────────────────────────────────▼────────────────────────────────────┐   │
│  │                        BRIDGE LAYER                                  │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │   tRPC-Flask Bridge (TypeScript)                              │   │   │
│  │  │   - Type-safe procedure calls                                 │   │   │
│  │  │   - Request/response transformation                           │   │   │
│  │  │   - Authentication forwarding                                 │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  └────────────────────────────────┬────────────────────────────────────┘   │
│                                   │                                        │
│  ┌────────────────────────────────▼────────────────────────────────────┐   │
│  │                        BACKEND LAYER                                 │   │
│  │                                                                      │   │
│  │  ┌─────────────────────────────────────────────────────────────┐    │   │
│  │  │   Flask API Server (Port 11436)                              │    │   │
│  │  │   - REST endpoints                                           │    │   │
│  │  │   - CORS enabled                                             │    │   │
│  │  │   - JSON request/response                                    │    │   │
│  │  └─────────────────────────────────────────────────────────────┘    │   │
│  │                                                                      │   │
│  │  ┌──────────────────────┐  ┌──────────────────────────────────────┐ │   │
│  │  │   KISWARM5.0         │  │   KIBank (NEW)                       │ │   │
│  │  │   ─────────────      │  │   ─────────────                      │ │   │
│  │  │   57 Modules         │  │   M60: Authentication                │ │   │
│  │  │   360+ Endpoints     │  │   M61: Banking Operations            │ │   │
│  │  │   - Sentinel Bridge  │  │   M62: Investment & Reputation       │ │   │
│  │  │   - HexStrike Guard  │  │   24 New Endpoints                   │ │   │
│  │  │   - Byzantine Agg.   │  │                                      │ │   │
│  │  │   - Crypto Ledger    │  │                                      │ │   │
│  │  │   - ... all others   │  │                                      │ │   │
│  │  └──────────────────────┘  └──────────────────────────────────────┘ │   │
│  │                                                                      │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Module Architecture

### KISWARM5.0 Modules (UNCHANGED)

| Version | Modules | Key Features |
|---------|---------|--------------|
| v5.1 | 34-38 | Solar Chase, Planetary Machine |
| v5.0 | 31-33 | HexStrike Guard, ToolForge, KiInstall |
| v4.3 | 29-30 | ICS Cybersecurity, OT Network Monitor |
| v4.2 | 24-28 | XAI, Predictive Maintenance, SIL |
| v4.1 | 17-23 | TD3 Controller, Formal Verification, Governance |
| v4.0 | 11-16 | CIEC Core (PLC, SCADA, Twin, Rules) |
| v3.0 | 7-10 | Fuzzy Tuner, Constrained RL, Digital Twin, Mesh |
| v2.2 | 1-6 | Intelligence Modules (Conflict, Decay, Ledger, etc.) |

### KIBank Modules (NEW)

#### M60: Authentication Module
- OAuth 2.0 Authorization Code Flow
- KI-Entity Cryptographic Identity
- Session Management with Permissions
- Token Refresh Mechanism

#### M61: Banking Operations Module
- Multi-currency Account Management
- Internal Transfers (instant settlement)
- SEPA Credit Transfers
- Transaction Validation & History

#### M62: Investment & Reputation Module
- Investment Portfolio Management
- Reputation Scoring (0-1000 scale)
- Trading Limits based on Reputation
- KI-Proof Verification Integration

## Security Architecture

### Transaction Security Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      TRANSACTION SECURITY PIPELINE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. AUTHENTICATION (M60)                                                    │
│     ├─ OAuth / KI-Entity verification                                      │
│     ├─ Session validation                                                  │
│     └─ Permission check                                                    │
│                                                                             │
│  2. SECURITY SCAN (M31 - HexStrike Guard)                                  │
│     ├─ Fraud detection                                                     │
│     ├─ Pattern analysis                                                    │
│     └─ Threat assessment                                                   │
│                                                                             │
│  3. BYZANTINE VALIDATION (M22)                                             │
│     ├─ N≥3f+1 consensus                                                    │
│     ├─ Gradient aggregation                                                │
│     └─ Anomaly detection                                                   │
│                                                                             │
│  4. CRYPTOGRAPHIC LEDGER (M4)                                              │
│     ├─ SHA-256 signing                                                     │
│     ├─ Merkle tree update                                                  │
│     └─ Audit trail                                                         │
│                                                                             │
│  5. REPUTATION UPDATE (M62)                                                │
│     ├─ Score calculation                                                   │
│     ├─ Tier update                                                         │
│     └─ Trading limit adjustment                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Data Flow

### Request Flow (Frontend → Backend)

```
User Action
    │
    ▼
React Component
    │
    ▼
tRPC Procedure Call
    │
    ▼
tRPC-Flask Bridge
    │
    ▼
Flask API Endpoint
    │
    ├─► KIBank Module (M60/M61/M62)
    │       │
    │       ├─► Validation
    │       ├─► Business Logic
    │       ├─► Security Integration
    │       └─► Response
    │
    └─► Sentinel Module (M1-M38)
            │
            └─► Response
```

### Response Flow (Backend → Frontend)

```
Module Response
    │
    ▼
Flask JSON Response
    │
    ▼
tRPC Bridge Transformation
    │
    ▼
TypeScript Type Inference
    │
    ▼
React State Update
    │
    ▼
UI Render
```

## Technology Stack

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| React | 18 | UI Framework |
| TypeScript | 5 | Type Safety |
| Vite | 7 | Build Tool |
| tRPC | 11 | API Layer |
| TanStack Query | 5 | Data Fetching |
| Tailwind CSS | 4 | Styling |
| shadcn/ui | latest | UI Components |

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.10+ | Runtime |
| Flask | 3.0 | Web Framework |
| Ollama | latest | LLM Runtime |
| Qdrant | 1.7+ | Vector DB |
| sentence-transformers | 2.7+ | Embeddings |

### Bridge
| Technology | Version | Purpose |
|------------|---------|---------|
| TypeScript | 5 | Type Safety |
| tRPC Server | 11 | API Server |
| Express | 4 | HTTP Server |
| Axios | 1 | HTTP Client |

## Deployment Architecture

### Development
```
Frontend (Vite dev server)  →  Port 3000
    │
    └──► Bridge (tsx watch)  →  Port 3001
              │
              └──► Backend (Flask)  →  Port 11436
```

### Production
```
Frontend (static files)  →  CDN / S3
    │
    └──► Bridge (Node.js)  →  Port 3000
              │
              └──► Backend (Gunicorn)  →  Port 11436
```

## Scalability

### Horizontal Scaling
- Frontend: Static files served from CDN
- Bridge: Multiple instances behind load balancer
- Backend: Multiple Flask workers with Gunicorn

### Vertical Scaling
- Backend: Increase Python worker processes
- Bridge: Increase Node.js memory/threads
- Database: Scale Qdrant cluster

## Security Considerations

1. **Authentication**
   - All requests require valid session token
   - Token expiration and refresh mechanism
   - Permission-based access control

2. **Transport Security**
   - HTTPS required in production
   - CORS configured for allowed origins
   - Rate limiting on public endpoints

3. **Data Security**
   - No raw data leaves the system
   - Cryptographic audit trail
   - Merkle tree integrity verification

4. **Compliance**
   - SEPA payment regulations
   - Data privacy (GDPR compatible)
   - Financial services standards
