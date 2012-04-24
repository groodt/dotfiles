# various additional completions
# http://www.gnu.org/software/bash/manual/bashref.html#Programmable-Completion-Builtins

# Add bash completion for ssh: it tries to complete the host to which you
# want to connect from the list of the ones contained in ~/.ssh/known_hosts
__ssh_known_hosts() {
if [[ -f ~/.ssh/known_hosts ]]; then
cut -d " " -f1 ~/.ssh/known_hosts | cut -d "," -f1
fi
}

_known_hosts() {
local cur known_hosts
COMPREPLY=()
cur="${COMP_WORDS[COMP_CWORD]}"
known_hosts="$(__ssh_known_hosts)"

if [[ ! ${cur} == -* ]] ; then
COMPREPLY=( $(compgen -W "${known_hosts}" -- ${cur}) )
return 0
fi
}

complete -F _known_hosts whois nslookup nmap ssh
complete -F _known_hosts push_ssh_cert

#killall
complete -o nospace -A command killall

# git-track completes remote names
complete -o default -o nospace -F _git_checkout git-track
