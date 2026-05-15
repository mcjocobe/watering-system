{
  lib,
  buildNpmPackage,
  stdenv,
}: let
  build-result = buildNpmPackage {
    pname = "ui";
    version = "1.0.0";

    src = ./src/ui/watering-system;

    npmDepsHash = "sha256-ltWimdQmvAqwJj8DJFUxBkMiDWQd/BPbp+W3mprFCBI=";
  };
in
  stdenv.mkDerivation {
    name = "water-system-ui";
    src = build-result;

    installPhase = ''
      cp -r lib/node_modules/ui/dist $out/
    '';
  }
