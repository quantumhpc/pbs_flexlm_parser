# PBS Pro FlexLM License Parser
Flexlm parser for PBS Pro to integrate license aware scheduling.

## Usage

Modify the script to add the full path to **lmutil** and use it inside pbs scheduler _sched_config_ with

```
lmparser.py -f feature_name -c port@licserver
```

Exemple:
```
server_dyn_res: "hpcdomains !/var/spool/pbs/server_priv/scripts/lmparser.py -f hpcdomains -c 1999@lic_server"
```
