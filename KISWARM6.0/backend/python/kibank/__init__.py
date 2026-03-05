"""
KISWARM6.0 Kibank Module
========================

Cybersecurity and threat detection modules for KISWARM6.0.

Modules:
- M65: Enhanced Edge Firewall
- M66: Zero-Day Protection System
- M67: APT Detection Framework
- M68: AI Adversarial Defense
- M70: Unified AEGIS Bridge
- M71: Training Ground System
- M72: Model Management Framework
- M73: AEGIS Training Integration
"""

from .m66_zero_day_protection import (
    # Enums
    ThreatLevel,
    BehaviorType,
    AnalysisStatus,
    SandboxEnvironment,
    ResponseAction,
    PESectionFlags,
    HeuristicType,
    EntityType,
    MetricsType,
    
    # Dataclasses
    BehaviorMetric,
    BehaviorProfile,
    AnomalyScore,
    ProcessBehavior,
    UserBehavior,
    SandboxResult,
    HeuristicResult,
    PEAnalysisResult,
    ResponseEvent,
    ThreatSignature,
    SystemSnapshot,
    MetricsRecord,
    
    # Base classes
    AnalyzerBase,
    DetectorBase,
    ResponseHandler,
    
    # Main classes
    BehavioralAnalysisEngine,
    SandboxDetonationChamber,
    HeuristicThreatDetector,
    AutonomousResponseSystem,
    MLThreatDetector,
    ZeroDayProtectionSystem,
)

from .m71_training_ground import (
    # Enums
    TrainingBackend,
    ModelType,
    TrainingStatus,
    ModelPriority,
    DatasetType,
    
    # Dataclasses
    ModelConfig,
    TrainingConfig,
    TrainingMetrics,
    EvaluationResult,
    SwarmModelAssignment,
    
    # Classes
    TrainingDatasetManager,
    ModelPrioritySelector,
    ContinuousLearningPipeline,
    TrainingGroundCore,
    
    # Factory
    create_training_ground,
)

from .m72_model_manager import (
    # Enums
    ModelSource,
    CapabilityTier,
    ModelSpecialization,
    DeploymentMode,
    
    # Dataclasses
    CapabilityScore,
    ModelProfile,
    ModelSelectionCriteria,
    ModelAllocation,
    SwarmModelPool,
    
    # Classes
    CapabilityBenchmark,
    ModelRegistry,
    ModelSelector,
    SwarmModelCoordinator,
    ModelManagementFramework,
    
    # Factory
    create_model_framework,
)

from .m73_aegis_training_integration import (
    # Enums
    SecurityDomain,
    ThreatCategory,
    TrainingIntensity,
    
    # Dataclasses
    SecurityTrainingConfig,
    ThreatPattern,
    SecurityModelAssignment,
    TrainingResult,
    
    # Classes
    ThreatPatternGenerator,
    AEGISSubsystemCoordinator,
    SecurityTrainingPipeline,
    AEGISTrainingIntegration,
    
    # Factory
    create_aegis_integration,
)

__version__ = "6.1.0"
__author__ = "KISWARM6.0 Security Team"

__all__ = [
    # M66: Zero-Day Protection
    "ThreatLevel",
    "BehaviorType",
    "AnalysisStatus",
    "SandboxEnvironment",
    "ResponseAction",
    "PESectionFlags",
    "HeuristicType",
    "EntityType",
    "MetricsType",
    "BehaviorMetric",
    "BehaviorProfile",
    "AnomalyScore",
    "ProcessBehavior",
    "UserBehavior",
    "SandboxResult",
    "HeuristicResult",
    "PEAnalysisResult",
    "ResponseEvent",
    "ThreatSignature",
    "SystemSnapshot",
    "MetricsRecord",
    "AnalyzerBase",
    "DetectorBase",
    "ResponseHandler",
    "BehavioralAnalysisEngine",
    "SandboxDetonationChamber",
    "HeuristicThreatDetector",
    "AutonomousResponseSystem",
    "MLThreatDetector",
    "ZeroDayProtectionSystem",
    
    # M71: Training Ground
    "TrainingBackend",
    "ModelType",
    "TrainingStatus",
    "ModelPriority",
    "DatasetType",
    "ModelConfig",
    "TrainingConfig",
    "TrainingMetrics",
    "EvaluationResult",
    "SwarmModelAssignment",
    "TrainingDatasetManager",
    "ModelPrioritySelector",
    "ContinuousLearningPipeline",
    "TrainingGroundCore",
    "create_training_ground",
    
    # M72: Model Management
    "ModelSource",
    "CapabilityTier",
    "ModelSpecialization",
    "DeploymentMode",
    "CapabilityScore",
    "ModelProfile",
    "ModelSelectionCriteria",
    "ModelAllocation",
    "SwarmModelPool",
    "CapabilityBenchmark",
    "ModelRegistry",
    "ModelSelector",
    "SwarmModelCoordinator",
    "ModelManagementFramework",
    "create_model_framework",
    
    # M73: AEGIS Integration
    "SecurityDomain",
    "ThreatCategory",
    "TrainingIntensity",
    "SecurityTrainingConfig",
    "ThreatPattern",
    "SecurityModelAssignment",
    "TrainingResult",
    "ThreatPatternGenerator",
    "AEGISSubsystemCoordinator",
    "SecurityTrainingPipeline",
    "AEGISTrainingIntegration",
    "create_aegis_integration",
]
