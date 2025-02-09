# Cross-Platform Command Implementations

## Initialization and Backup Procedures

### Operating System Compatibility

This document provides cross-platform command implementations for different operating systems.

### Windows (PowerShell)

#### Initialization Command

```powershell
function Initialize-WindsurfSession {
    $backup_dir = "${env:USERPROFILE}\.windsurf\backups"
    $global_rules_path = "${env:USERPROFILE}\.codeium\windsurf\memories\global_rules.md"
    
    # Ensure backup directory exists
    if (!(Test-Path -Path $backup_dir)) {
        New-Item -ItemType Directory -Force -Path $backup_dir
    }
    
    # Restore last valid APS
    $last_valid_aps = Get-ChildItem $backup_dir | 
        Where-Object { $_.Name -like "*_APS.md" } | 
        Sort-Object LastWriteTime -Descending | 
        Select-Object -First 1
    
    if ($last_valid_aps) {
        Copy-Item $last_valid_aps.FullName -Destination $global_rules_path
    }
}
```

#### Save and Backup Command

```powershell
function Save-WindsurfContext {
    $backup_dir = "${env:USERPROFILE}\.windsurf\backups"
    $global_rules_path = "${env:USERPROFILE}\.codeium\windsurf\memories\global_rules.md"
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    
    # Ensure backup directory exists
    if (!(Test-Path -Path $backup_dir)) {
        New-Item -ItemType Directory -Force -Path $backup_dir
    }
    
    # Backup current global rules
    Copy-Item $global_rules_path -Destination "$backup_dir\${timestamp}_APS.md"
    
    # Optional: Update APS sections (placeholder for future implementation)
    # Update-APSSections -GlobalRulesPath $global_rules_path
}
```

### macOS/Linux (Bash)

#### Initialization Command

```bash
function windsurf_init() {
    BACKUP_DIR="${HOME}/.windsurf/backups"
    GLOBAL_RULES_PATH="${HOME}/.codeium/windsurf/memories/global_rules.md"
    
    # Ensure backup directory exists
    mkdir -p "$BACKUP_DIR"
    
    # Find and restore most recent backup
    LAST_VALID_APS=$(find "$BACKUP_DIR" -name "*_APS.md" -print0 | xargs -0 ls -t | head -1)
    
    if [ -f "$LAST_VALID_APS" ]; then
        cp "$LAST_VALID_APS" "$GLOBAL_RULES_PATH"
    fi
}
```

#### Save and Backup Command

```bash
function windsurf_save() {
    BACKUP_DIR="${HOME}/.windsurf/backups"
    GLOBAL_RULES_PATH="${HOME}/.codeium/windsurf/memories/global_rules.md"
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    
    # Ensure backup directory exists
    mkdir -p "$BACKUP_DIR"
    
    # Backup current global rules
    cp "$GLOBAL_RULES_PATH" "$BACKUP_DIR/${TIMESTAMP}_APS.md"
}
```

## Usage Guidelines

1. Source these functions in your shell initialization script
2. Call `Initialize-WindsurfSession` (PowerShell) or `windsurf_init` (Bash) at the start of each session
3. Use `Save-WindsurfContext` or `windsurf_save` to backup project state

## Customization

- Modify paths as needed for your specific setup
- Add additional logging or error handling as required
- Extend functions to include more sophisticated APS management

## Future Improvements

- Implement cross-platform APS update mechanism
- Add more robust error checking
- Create a unified interface for different operating systems
