set -U EDITOR nvim
alias vi="nvim"
alias vim="nvim"

alias bt="bash ~/bluetooth-mic.sh"
alias nb="jupyter notebook"

alias env-dl="source ~/envs/dl/bin/activate"
alias env-ga="source ~/envs/ga/bin/activate"
alias env-base="deactivate"

contains /usr/local/cuda-11.1/bin $fish_user_paths; or set -Ua fish_user_paths /usr/local/cuda-11.1/bin
contains ~/.local/bin $fish_user_paths; or set -Ua fish_user_paths ~/.local/bin

neofetch

