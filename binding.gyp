{
  "targets": [
    {
      "target_name": "bitwebyespowernative",
      "sources": [ "src/bitweb_yespower.cc",
                "src/yespower-1.0.0/yespower.c",
                "src/yespower-1.0.0/yespower-opt.c",
                "src/yespower-1.0.0/sha256.c",
      ],
      "include_dirs": ["<!@(node -p \"require('node-addon-api').include\")"],
      "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "CLANG_CXX_LIBRARY": "libc++",
        "MACOSX_DEPLOYMENT_TARGET": "10.7"
      },
      "msvs_settings": {
        "VCCLCompilerTool": { "ExceptionHandling": 1 },
      }
    }
  ],
  "include": ["<!(node -p \"require('node-addon-api').gyp\")"]
}
