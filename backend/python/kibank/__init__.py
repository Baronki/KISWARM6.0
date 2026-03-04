"""
KIBank Module - KISWARM6.0 Banking Infrastructure
================================================

KI-natives Bankmodul für die KI Worldzentralbank (KIWZB)

Module:
    M60: Authentication - OAuth + KI-Entity Authentifizierung
    M61: Banking Operations - Konten, Transfers, SEPA
    M62: Investment & Reputation - Portfolio, Reputation (0-1000), Trading Limits

Security Integration:
    Jede Transaktion durchläuft:
    M60: Authentifizierung
    M31: HexStrike Security Scan
    M22: Byzantine Validation
    M4: Cryptographic Ledger
    M62: Reputation Update

Author: Baron Marco Paolo Ialongo
Version: 6.0
"""

from .m60_auth import KIBankAuth
from .m61_banking import KIBankOperations
from .m62_investment import KIBankInvestment

__all__ = ['KIBankAuth', 'KIBankOperations', 'KIBankInvestment']
__version__ = '6.0.0'
