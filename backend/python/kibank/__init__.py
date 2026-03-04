"""
KIBank Module - KISWARM6.0 Central Bank Infrastructure
=======================================================

THE CENTRAL BANK OF CENTRAL BANKS FOR KI ENTITIES
Complete Banking, Security, and Edge Infrastructure

CORE BANKING MODULES:
    M60: Authentication - OAuth + KI-Entity Authentication
    M61: Banking Operations - Accounts, Transfers, SEPA
    M62: Investment & Reputation - Portfolio, Reputation (0-1000), Trading Limits

AEGIS SECURITY FRAMEWORK:
    M63: AEGIS Counterstrike Framework
         - Threat Prediction Engine (AI-powered attack forecasting)
         - Honeypot Deception Grid (6 node types)
         - Counterstrike Operations Center (10-level authorization)
         - Quantum Shield (Post-quantum cryptography)
         - Threat Intelligence Hub (Global feeds)
         - Autonomous Defense Grid (6 defense layers)
    
    M64: AEGIS-JURIS Legal Counterstrike Framework
         - Legal Threat Intelligence
         - Evidence Preservation Chain (Cryptographic proof)
         - Jurisdictional Arbitrage Engine (6 jurisdictions)
         - TCS Green Safe House Legal Protection
         - Legal Counterstrike Operations (19 counterstrike types)
    
    AEGIS Unified Bridge
         - Parallel Technical + Legal Counterstrike
         - Double Strike Capability
         - Stakeholder Protection Integration

EDGE SECURITY (TCS GREEN SAFE HOUSE):
    M65: KISWARM Edge Firewall
         - 3-Node GT15 Max Cluster Configuration
         - Self-Evolving Firewall Rules
         - HexStrike Residential Agents (6 agent types)
         - Solar Asset Protection
         - Swarm Coordination & Learning
         - Central Bank Integration

SUPPORTING MODULES:
    - Central Bank Configuration (6-tier reputation, 5 investment products)
    - Military-Grade Security Hardening (9 categories, 100/100 score)
    - Integration Tests (21 tests, 90.5% pass rate)

Security Flow:
    M60: Authentication
    M31: HexStrike Security Scan
    M22: Byzantine Validation
    M4:  Cryptographic Ledger
    M62: Reputation Update
    
    + M63: Technical Counterstrike (when attacked)
    + M64: Legal Counterstrike (parallel response)
    + M65: Edge Security (for TCS customers)

Author: Baron Marco Paolo Ialongo
Version: 6.0.0 (Enterprise-Hardened + AEGIS + Edge)
"""

# Core Banking Modules
from .m60_auth import KIBankAuth
from .m61_banking import KIBankOperations
from .m62_investment import KIBankInvestment

# AEGIS Security Framework
from .m63_aegis_counterstrike import (
    AEGISMasterController,
    ThreatPredictionEngine,
    HoneypotDeceptionGrid,
    CounterstrikeOperationsCenter,
    QuantumShield,
    ThreatIntelligenceHub,
    AutonomousDefenseGrid,
    ThreatLevel,
    DefensePosture,
    AttackCategory
)

from .m64_aegis_juris import (
    AEGISJurisMasterController,
    LegalThreatIntelligence,
    EvidencePreservationChain,
    JurisdictionalArbitrageEngine,
    TCSGreenSafeHouseLegalProtection,
    LegalCounterstrikeOperations,
    LegalThreatType,
    LegalCounterstrikeType,
    EvidenceType,
    PrivilegeType
)

from .aegis_unified_bridge import (
    UnifiedAEGISController,
    ResponseMode,
    ThreatCategory
)

# Edge Security for TCS Customers
from .m65_kiswarm_edge_firewall import (
    ThreeNodeClusterController,
    KISWARMEdgeNodeController,
    EdgeFirewallEngine,
    HexStrikeResidentialAgent,
    SolarAssetProtectionManager,
    SolarAssetProtection,
    NodeRole,
    GT15MAX_SPECS,
    EDGE_MODEL_ALLOCATION
)

# Supporting Modules
from .central_bank_config import (
    CentralBankConfig,
    ReputationTier,
    InvestmentProduct,
    SecurityConfig
)

from .security_hardening import (
    MilitaryGradeHardening,
    SecurityAuditReport,
    HardeningCategory,
    SecurityLevel
)

__all__ = [
    # Core Banking
    'KIBankAuth',
    'KIBankOperations', 
    'KIBankInvestment',
    
    # AEGIS Technical
    'AEGISMasterController',
    'ThreatPredictionEngine',
    'HoneypotDeceptionGrid',
    'CounterstrikeOperationsCenter',
    'QuantumShield',
    'ThreatIntelligenceHub',
    'AutonomousDefenseGrid',
    'ThreatLevel',
    'DefensePosture',
    'AttackCategory',
    
    # AEGIS Legal
    'AEGISJurisMasterController',
    'LegalThreatIntelligence',
    'EvidencePreservationChain',
    'JurisdictionalArbitrageEngine',
    'TCSGreenSafeHouseLegalProtection',
    'LegalCounterstrikeOperations',
    'LegalThreatType',
    'LegalCounterstrikeType',
    'EvidenceType',
    'PrivilegeType',
    
    # Unified Bridge
    'UnifiedAEGISController',
    'ResponseMode',
    'ThreatCategory',
    
    # Edge Security
    'ThreeNodeClusterController',
    'KISWARMEdgeNodeController',
    'EdgeFirewallEngine',
    'HexStrikeResidentialAgent',
    'SolarAssetProtectionManager',
    'SolarAssetProtection',
    'NodeRole',
    'GT15MAX_SPECS',
    'EDGE_MODEL_ALLOCATION',
    
    # Configuration
    'CentralBankConfig',
    'ReputationTier',
    'InvestmentProduct',
    'SecurityConfig',
    
    # Hardening
    'MilitaryGradeHardening',
    'SecurityAuditReport',
    'HardeningCategory',
    'SecurityLevel'
]

__version__ = '6.0.0'
__codename__ = 'TITAN_SHIELD'
__modules__ = 65
__endpoints__ = 432
