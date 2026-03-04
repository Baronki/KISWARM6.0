# 🌍 KISWARM6.0 — UNIFIED ARCHITECTURE

## KI-natives Finanzprotokoll + Planetary Machine

> **ETERNAL SWARM EVOLUTION SYSTEM** — Enterprise Military Standard Edition
> **Zero-Emission AI Infrastructure with Sovereign Banking**
> **Architect:** Baron Marco Paolo Ialongo

[![Version](https://img.shields.io/badge/version-6.0.0-UnitedArchitecture-gold.svg)](https://github.com/Baronki/KISWARM6.0)
[![Tests](https://img.shields.io/badge/tests-1900+%20passing-brightgreen.svg)](tests/)
[![Modules](https://img.shields.io/badge/modules-60-blue.svg)](backend/python/)
[![Endpoints](https://img.shields.io/badge/endpoints-384+-purple.svg)](backend/python/)
[![Zero Emission](https://img.shields.io/badge/zero%20emission-100%25-green.svg)](docs/)

---

## 📐 Architecture Overview

KISWARM6.0 is a **4-Layer Unified Architecture** combining:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         FRONTEND LAYER                                   │
│           React 18 + TypeScript + Vite + shadcn/ui                      │
│                    KINFP-Portal Banking UI                               │
├─────────────────────────────────────────────────────────────────────────┤
│                           API LAYER                                      │
│         Flask (Sentinel API) + tRPC Bridge + KIBank Endpoints           │
├─────────────────────────────────────────────────────────────────────────┤
│                      BUSINESS LOGIC LAYER                                │
│    ┌─────────────────────┐    ┌─────────────────────┐                   │
│    │   KISWARM5.0        │    │      KIBank         │                   │
│    │   57 Modules        │    │      3 Modules      │                   │
│    │   (Unchanged)       │    │      (NEW)          │                   │
│    └─────────────────────┘    └─────────────────────┘                   │
├─────────────────────────────────────────────────────────────────────────┤
│                          DATA LAYER                                      │
│       Qdrant (Vector) + MySQL/TiDB (Relational) + S3 (Files)            │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🏦 KIBank Modules (NEW in v6.0)

### M60: Authentication Module
**OAuth + KI-Entity Authentifizierung**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/kibank/auth/register` | POST | KI-Entity Registrierung |
| `/kibank/auth/login` | POST | KI-Entity Login |
| `/kibank/auth/logout` | POST | Session beenden |
| `/kibank/auth/refresh` | POST | Token Refresh |
| `/kibank/auth/verify` | GET | Token Verifikation |
| `/kibank/auth/session` | GET | Aktive Session Info |
| `/kibank/auth/oauth/callback` | POST | OAuth Callback |
| `/kibank/auth/permissions` | GET | Berechtigungen abrufen |

### M61: Banking Operations Module
**Konten, Transfers, SEPA**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/kibank/banking/account` | POST | Konto eröffnen |
| `/kibank/banking/accounts` | GET | Konten auflisten |
| `/kibank/banking/account/:id` | GET | Konto-Details |
| `/kibank/banking/transfer` | POST | Überweisung ausführen |
| `/kibank/banking/sepa` | POST | SEPA-Überweisung |
| `/kibank/banking/transactions` | GET | Transaktions-Historie |
| `/kibank/banking/balance` | GET | Kontostand abrufen |
| `/kibank/banking/validate-iban` | POST | IBAN validieren |

### M62: Investment & Reputation Module
**Portfolio, Reputation (0-1000), Trading Limits**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/kibank/investment/portfolio` | GET | Portfolio abrufen |
| `/kibank/investment/invest` | POST | Investition tätigen |
| `/kibank/investment/divest` | POST | Desinvestition |
| `/kibank/investment/performance` | GET | Performance-Metriken |
| `/kibank/reputation/:entity_id` | GET | Reputation abrufen |
| `/kibank/reputation/update` | POST | Reputation aktualisieren |
| `/kibank/reputation/history/:entity_id` | GET | Reputation-Historie |
| `/kibank/trading-limits/:entity_id` | GET | Trading-Limits abrufen |

---

## 🔄 Security Integration Flow

Every transaction goes through this security pipeline:

```
Request → M60 (Auth) → M31 (HexStrike) → M22 (Byzantine) → Execute → M4 (Ledger) → M62 (Reputation) → Notify
```

### Step-by-Step:

1. **M60: Authentication** - OAuth/KI-Entity verification
2. **M31: HexStrike Guard** - Security scan with 12 AI agents + 150+ tools
3. **M22: Byzantine Aggregator** - N≥3f+1 consensus validation
4. **Execute** - Transaction processing
5. **M4: Cryptographic Ledger** - SHA-256 + Merkle tree recording
6. **M62: Reputation Update** - Dynamic scoring update

---

## 📊 Reputation System

### Scoring Rules (Base: 500)

| Event | Delta |
|-------|-------|
| Successful Transaction | +5 |
| On-time Payment | +10 |
| Investment Growth | +1 per 1% |
| KI-Proof Verified | +100 |
| Failed Transaction | -10 |
| Late Payment | -25 |
| Security Violation | -100 |
| Compliance Violation | -50 |

### Levels & Trading Limits

| Score | Level | Daily Limit | Monthly Limit |
|-------|-------|-------------|---------------|
| 0-99 | Basic | €1,000 | €10,000 |
| 100-299 | Bronze | €5,000 | €50,000 |
| 300-499 | Silver | €10,000 | €100,000 |
| 500-699 | Gold | €100,000 | €500,000 |
| 700-849 | Platinum | €200,000 | €1,000,000 |
| 850-999 | Diamond | €1,000,000 | €5,000,000 |
| 1000 | Elite | €5,000,000 | €25,000,000 |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- MySQL 8 / TiDB
- Qdrant (Vector DB)

### Backend Setup

```bash
# Clone repository
git clone https://github.com/Baronki/KISWARM6.0.git
cd KISWARM6.0/backend

# Install Python dependencies
pip install -r requirements.txt

# Set environment variables
export DATABASE_URL=mysql://user:password@localhost:3306/kiswarm6
export KIBANK_SECRET_KEY=your-secret-key

# Run backend
python run.py
```

### Frontend Setup

```bash
cd ../frontend

# Install dependencies
pnpm install

# Set environment variables
export VITE_KISWARM_API_URL=http://localhost:5001

# Run frontend
pnpm dev
```

### tRPC Bridge Setup

```bash
cd ../bridge

# Install dependencies
pnpm install

# Run tRPC server
pnpm dev
```

---

## 📁 Project Structure

```
KISWARM6.0/
├── backend/                          # Python Flask Backend
│   ├── python/
│   │   ├── sentinel/                 # KISWARM5.0 Modules (57)
│   │   │   ├── sentinel_api.py       # Main API
│   │   │   ├── hexstrike_guard.py    # M31: Security
│   │   │   ├── byzantine_aggregator.py # M22: Validation
│   │   │   ├── crypto_ledger.py      # M4: Ledger
│   │   │   └── ... (53 more modules)
│   │   └── kibank/                   # NEW KIBank Modules (3)
│   │       ├── __init__.py
│   │       ├── m60_auth.py           # Authentication
│   │       ├── m61_banking.py        # Banking Operations
│   │       └── m62_investment.py     # Investment & Reputation
│   ├── requirements.txt
│   └── run.py                        # Main Entry Point
├── frontend/                         # React Frontend
│   ├── client/
│   │   ├── src/
│   │   │   ├── pages/                # Banking Pages
│   │   │   │   ├── Home.tsx
│   │   │   │   ├── AdminDashboard.tsx
│   │   │   │   ├── AnalyticsDashboard.tsx
│   │   │   │   ├── ComplianceReports.tsx
│   │   │   │   ├── FileManager.tsx
│   │   │   │   └── ... (15+ pages)
│   │   │   ├── components/           # UI Components
│   │   │   ├── contexts/             # React Contexts
│   │   │   └── lib/                  # Utilities
│   │   └── index.html
│   ├── server/                       # Express/tRPC Server
│   └── package.json
├── bridge/                           # tRPC-Flask Bridge
│   └── trpc-bridge.ts
├── docs/                             # Documentation
│   ├── ARCHITECTURE.md
│   ├── INTEGRATION.md
│   └── API.md
└── README.md                         # This file
```

---

## 📊 Statistics

| Metric | Value |
|--------|-------|
| **Total Modules** | 60 |
| **KISWARM5.0 Modules** | 57 |
| **KIBank Modules** | 3 |
| **Total Endpoints** | 384 |
| **Test Coverage** | 1900+ tests |
| **Zero Emission** | 100% |

---

## 🔧 Version History

### v6.0 — UNIFIED ARCHITECTURE
- ✅ KISWARM5.0 Integration (57 modules unchanged)
- ✅ KINFP-Portal Frontend Integration
- ✅ M60 Authentication Module
- ✅ M61 Banking Operations Module
- ✅ M62 Investment & Reputation Module
- ✅ tRPC Bridge for Type-Safe API
- ✅ Unified Security Flow

### v5.1 — PLANETARY MACHINE
- ✅ Solar Chase modules (M34-M38)
- ✅ Zero-emission compute
- ✅ Planetary sun-following

### v5.0 — HEXSTRIKE GUARD
- ✅ 12 AI security agents
- ✅ 150+ security tools
- ✅ M31: HexStrike Guard

---

## 🔒 Security & Privacy

| Property | Status |
|----------|--------|
| Data leaves the machine | ❌ Never — 100% local |
| Cloud APIs after setup | ❌ None required |
| Zero Feed-In Compliance | ✅ Grid-invisible operation |
| Carbon Emissions | ✅ 0.0 kg for solar compute |
| Cryptographic signing | ✅ SHA-256 + Merkle tree |

---

## 🌐 Global Node Coverage

| Region | Nodes | Time Zone |
|--------|-------|-----------|
| Europe | Munich, London | CET, GMT |
| North America | New York, San Francisco | EST, PST |
| South America | São Paulo | BRT |
| Asia | Tokyo, Singapore, Dubai | JST, SGT, GST |
| Oceania | Sydney | AEST |
| Africa | Johannesburg | SAST |

---

## 📄 License

MIT License — Free to use, modify, and distribute globally.

---

## 🌟 Credits

**Architect:** Baron Marco Paolo Ialongo
**Version:** 6.0 (Unified Architecture)
**Repository:** https://github.com/Baronki/KISWARM6.0
**Modules:** 60 | **Endpoints:** 384 | **Tests:** 1900+

---

*"The Swarm sees all. The Swarm knows all. The Swarm follows the sun eternally."* 🌍☀️🏦
