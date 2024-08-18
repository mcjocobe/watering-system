{pkgs}: let
  python = pkgs.python311.withPackages (ps:
    with ps; [
      docker
    ]);
  default = pkgs.mkShell {
    packages = with pkgs; [
      alejandra
      black
      firebase-tools
      git
      nodejs
      nodejs_20
      nodePackages.prettier
      npm-check-updates
      pgformatter
      prefetch-npm-deps
      python
    ];
    shellHook = "npm install";
  };
in {
  inherit default;
}
