# ollama packaging for fedora

## build locally
in the v0.3.6 build of ollama relies on a .so file that is linked in /lib however in Fedora x86_64 libraries usually are in /lib64 as such need to be recompiled as to run on fedora.

**Build documentation in:**
- https://github.com/ollama/ollama/tree/main/docs/development.md
**Build Scripts:**
- `scripts/rh_linux_deps.sh`
- `scripts/env.sh`
**Install Scripts**
- https://github.com/ollama/ollama/blob/main/scripts/install.sh

1. **build:**
`llm/generate/gen_linux.sh`

```bash
git clone --recurse-submodules git@github.com:ollama/ollama.git
cd ollama
OLLAMA_CUSTOM_CPU_DEFS="-DGGML_AVX=off -DGGML_AVX2=off -DGGML_F16C=off -DGGML_FMA=off" go generate ./...
go build .
```

2. **manual install:**
> Note: assumed that developer is inside local ollama folder.
```bash
# based of https://github.com/ollama/ollama/blob/main/docs/linux.md

# make ollama user
```bash
sudo useradd -r -s /bin/false -U -m -d /usr/share/ollama ollama
sudo usermod -a -G ollama $(whoami)
```

#  write Ollama service
```bash
sudo echo -e '[Unit]\nDescription=Ollama service\nAfter=network-online.target\n\n[Service]\nExecStart=/usr/bin/ollama serve\nUser=ollama\nGroup=ollama\nRestart=on-failure\nRestartSec=3\n\Environment="PATH=$PATH"n[Install]\nWantedBy=multi-user.target' > /etc/systemd/system/ollama.service
```
# enable and star start service
```bash
sudo systemctl daemon-reload
sudo systemctl enable ollama
sudo systemctl start ollama
```

- TODO

```

## Cuda:
**Note: I will not be doing a cuda build for fedora this are just general instructions**

**check what cuda aversion you have:**

can be checked with `nvidia-smi`
or this script that should output your cuda version:
```bash
nvidia-smi -q | awk '$0 ~ /CUDA Version[^\n]*/ {print $4}'
```

you can find full list of nvida container on:

**regestry:**

https://hub.docker.com/r/nvidia/cuda/tags

https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda

**ollama docker images**

https://hub.docker.com/r/ollama/ollama

**git repo:**

https://gitlab.com/nvidia/container-images/cuda/-/tree/master/dist

* then build with `nvidia-container-toolkit` 

## should ollama's registry be patched out?
- https://registry.ollama.ai/v2/library/{model}/manifests/latest

## dependencies needed for project
- https://github.com/spf13/cobra
### go.mod packages
        github.com/bytedance/sonic v1.11.6 // indirect
        github.com/gabriel-vasile/mimetype v1.4.3 // indirect
        github.com/gin-contrib/cors v1.7.2
        github.com/gin-contrib/sse v0.1.0 // indirect
        github.com/go-playground/locales v0.14.1 // indirect
        github.com/go-playground/universal-translator v0.18.1 // indirect
        github.com/go-playground/validator/v10 v10.20.0 // indirect
        github.com/goccy/go-json v0.10.2 // indirect
        github.com/inconshreveable/mousetrap v1.1.0 // indirect
        github.com/json-iterator/go v1.1.12 // indirect
        github.com/klauspost/cpuid/v2 v2.2.7 // indirect
        github.com/leodido/go-urn v1.4.0 // indirect
        github.com/mattn/go-isatty v0.0.20 // indirect
        github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
        github.com/modern-go/reflect2 v1.0.2 // indirect
        github.com/pelletier/go-toml/v2 v2.2.2 // indirect
        github.com/spf13/pflag v1.0.5 // indirect
        github.com/twitchyliquid64/golang-asm v0.15.1 // indirect
        github.com/ugorji/go/codec v1.2.12 // indirect
        golang.org/x/arch v0.8.0 // indirect
        golang.org/x/crypto v0.23.0
        golang.org/x/exp v0.0.0-20231110203233-9a3e6036ecaa
        golang.org/x/net v0.25.0 // indirect
        golang.org/x/sys v0.20.0
        golang.org/x/term v0.20.0
        golang.org/x/text v0.15.0
        google.golang.org/protobuf v1.34.1
        gopkg.in/yaml.v3 v3.0.1 // indirect
        github.com/apache/arrow/go/arrow v0.0.0-20211112161151-bc219186db40 // indirect
        github.com/bytedance/sonic/loader v0.1.1 // indirect
        github.com/chewxy/hm v1.0.0 // indirect
        github.com/chewxy/math32 v1.10.1 // indirect
        github.com/cloudwego/base64x v0.1.4 // indirect
        github.com/cloudwego/iasm v0.2.0 // indirect
        github.com/davecgh/go-spew v1.1.1 // indirect
        github.com/gogo/protobuf v1.3.2 // indirect
        github.com/google/flatbuffers v24.3.25+incompatible // indirect
        github.com/kr/text v0.2.0 // indirect
        github.com/pkg/errors v0.9.1 // indirect
        github.com/pmezard/go-difflib v1.0.0 // indirect
        github.com/rivo/uniseg v0.2.0 // indirect
        github.com/xtgo/set v1.0.0 // indirect
        go4.org/unsafe/assume-no-moving-gc v0.0.0-20231121144256-b99613f794b6 // indirect
        golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1 // indirect
        gonum.org/v1/gonum v0.15.0 // indirect
        gorgonia.org/vecf32 v0.9.0 // indirect
        gorgonia.org/vecf64 v0.9.0 // indirect
        github.com/agnivade/levenshtein v1.1.1
        github.com/d4l3k/go-bfloat16 v0.0.0-20211005043715-690c3bdd05f1
        github.com/google/go-cmp v0.6.0
        github.com/mattn/go-runewidth v0.0.14
        github.com/nlpodyssey/gopickle v0.3.0
        github.com/pdevine/tensor v0.0.0-20240510204454-f88f4562727c
        github.com/containerd/console v1.0.3
        github.com/emirpasic/gods v1.18.1
        github.com/gin-gonic/gin v1.10.0
        github.com/golang/protobuf v1.5.4 // indirect
        github.com/google/uuid v1.1.2
        github.com/olekukonko/tablewriter v0.0.5
        github.com/spf13/cobra v1.7.0
        github.com/stretchr/testify v1.9.0
        github.com/x448/float16 v0.8.4
        golang.org/x/sync v0.3.0

## Address model location:

- store models in `%_sharedstatedir/ollama` instead of `/usr/share/ollama/`
- look in to `xdg portal` use for Home directory:
    1. https://github.com/ollama/ollama/pull/897
    2. https://github.com/ollama/ollama/issues/228

## support x86_64_{1,2,3,4} cpu generations in `llama-cpp` or other packages:
1. **SDL3 in llama-cpp**

upstream the use of:

    1. https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h
    2. https://github.com/libsdl-org/SDL/blob/main/src/cpuinfo/SDL_cpuinfo.c

- reference: https://github.com/libsdl-org/SDL/blob/main/CMakeLists.txt
```
set_option(SDL_ASSEMBLY            "Enable assembly routines" ${SDL_ASSEMBLY_DEFAULT})
dep_option(SDL_AVX                 "Use AVX assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_X86 OR SDL_CPU_X64" OFF)
dep_option(SDL_AVX2                "Use AVX2 assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_X86 OR SDL_CPU_X64" OFF)
dep_option(SDL_AVX512F             "Use AVX512F assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_X86 OR SDL_CPU_X64" OFF)
dep_option(SDL_SSE                 "Use SSE assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_X86 OR SDL_CPU_X64" OFF)
dep_option(SDL_SSE2                "Use SSE2 assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_X86 OR SDL_CPU_X64" OFF)
dep_option(SDL_SSE3                "Use SSE3 assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_X86 OR SDL_CPU_X64" OFF)
dep_option(SDL_SSE4_1              "Use SSE4.1 assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_X86 OR SDL_CPU_X64" OFF)
dep_option(SDL_SSE4_2              "Use SSE4.2 assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_X86 OR SDL_CPU_X64" OFF)
dep_option(SDL_MMX                 "Use MMX assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_X86 OR SDL_CPU_X64" OFF)
dep_option(SDL_ALTIVEC             "Use Altivec assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_POWERPC32 OR SDL_CPU_POWERPC64" OFF)
dep_option(SDL_ARMSIMD             "Use SIMD assembly blitters on ARM" OFF "SDL_ASSEMBLY;SDL_CPU_ARM32" OFF)
dep_option(SDL_ARMNEON             "Use NEON assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_ARM32 OR SDL_CPU_ARM64" OFF)
dep_option(SDL_LSX                 "Use LSX assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_LOONGARCH64" OFF)
dep_option(SDL_LASX                "Use LASX assembly routines" ON "SDL_ASSEMBLY;SDL_CPU_LOONGARCH64" OFF)
```

2. **At runtime:**
- https://github.com/google/cpu_features

3. **Mailing list with useful info:**
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/EA6Y5AUE5DQ4WTD225L4UYMVXFTTK5UV/

4. **NDK:**
- https://android.googlesource.com/platform/ndk/+/main/sources/android/cpufeatures/cpu-features.h

5. **Archive reference:**
    1. https://github.com/intel/sgx-cpu-feature-detection/blob/master/README.md
    2. https://github.com/PhilipLudington/poshlib

6. **important conclusions:**
    1. dnf does support building for multiple cpu generation through --target x86_64_v?
    2. some changes needed to llama-cpp spec

~~**this may help with quantization:**~~
~~- https://github.com/ggerganov/llama.cpp/pull/8713~~

~~**Ollama builds in differnt directories:**~~
~~- `ollama/llm/build/linux/amd64/`~~

## Hardware Acceleration:
1. **Rocm:**
- Will most likly be in `Fedora 42` thanks to Tom

2. **Vulkan:**
- still in development in llama.cpp too soon to be added   
- `shaderc` package needed REF: ``

**Vulkan issues in Fedora:**
    1. https://bugzilla.redhat.com/show_bug.cgi?id=2314042
    2. Needs `expose "VK_DRIVER_FILES=/usr/share/vulkan/icd.d/nvidia_icd.json"` 
        + with `environment.d` https://www.man7.org/linux/man-pages/man5/environment.d.5.html
        + or with `setenv` https://man7.org/linux/man-pages/man3/setenv.3.html

**find problems with:**
- `libnvidia-vulkan-producer.so`
- `libnvidia-allocator.so`
- `controlD64`
- `vulkan/icd.d/nvidia_layers.json`

## Adding possible security features:
1. Remove all 0.0.0.0 interfaces:
`http://0.0.0.0` `https://0.0.0.0` `http://0.0.0.0:*` `https://0.0.0.0:*`
    + maybe able to fix with Environment verible:
    + https://github.com/ollama/ollama/blob/main/docs/faq.md#setting-environment-variables-on-linux
    + based on`llama/common.cpp` can be fixed by setting `LLAMA_ARG_HOST` evniroment varible
2. UsersAndGroups: https://docs.fedoraproject.org/en-US/packaging-guidelines/UsersAndGroups/
3. capabilities: https://man7.org/linux/man-pages/man7/capabilities.7.html
4. the systemd service will be isolated to `ollama` wheel group with out breaking functionality (read permission neads to be keapt).
    + Check out `rpmconf`
    + gidelines: https://docs.fedoraproject.org/en-US/packaging-guidelines/#_users_and_groups    
    + systemd: https://docs.fedoraproject.org/en-US/packaging-guidelines/Systemd/#definitions

## idea
- use ollama cmake to link with `lamma-cpp-devel` cmake as to build client packages like: `llama-cpp-rpc`, `llama-ccp-server` and custom patches https://github.com/ollama/ollama/tree/main/llm/patches
- Notes:
    + Check out `rpmconf`
    + gidelines:  https://docs.fedoraproject.org/en-US/packaging-guidelines/#_users_and_groups
    + systemd:    https://docs.fedoraproject.org/en-US/packaging-guidelines/Systemd/#definitions

~~test to see if we can just link `ollama serve` to `llama-cpp-server`.~~
- remove ssh keys (try to use llama-cpp cilent which will use curl to grab model form Hugging Face)
    + patching: https://docs.fedoraproject.org/en-US/packaging-guidelines/#_patch_guidelines

~~- patch out auto updating model functionality as to not connect to the internet without explicit user permission.~~

~~- setup cron for auto update functionality~~

~~+ https://docs.fedoraproject.org/en-US/packaging-guidelines/#_cron_files~~

~~+ https://docs.fedoraproject.org/en-US/packaging-guidelines/CronFiles/~~
