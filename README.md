# ollama packaging for fedora

## idea
- the systemd service will be isolated to `ollama` wheel group with out breaking functionality (read permission neads to be keapt).
    gidelines: https://docs.fedoraproject.org/en-US/packaging-guidelines/#_users_and_groups
    systemd: https://docs.fedoraproject.org/en-US/packaging-guidelines/Systemd/#definitions
- store models in `%_sharedstatedir/ollama` instead of `/usr/share/ollama/` (the direcory will also be isolate to the whealgroup).
    UsersAndGroups: https://docs.fedoraproject.org/en-US/packaging-guidelines/UsersAndGroups/
- test to see if we can just link `ollama serve` to `llama-cpp-server`.
- remove ssh keys (try to use llama-cpp cilent which will use curl to grab model form Hugging Face)
    patching: https://docs.fedoraproject.org/en-US/packaging-guidelines/#_patch_guidelines
- patch out auto updaing model functionality as to not connect to the internet without explicit user permission.
- setup cron for auto update functionality
    https://docs.fedoraproject.org/en-US/packaging-guidelines/#_cron_files
    https://docs.fedoraproject.org/en-US/packaging-guidelines/CronFiles/
