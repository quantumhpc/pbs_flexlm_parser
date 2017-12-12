# PBS Pro FlexLM License Parser
Flexlm parser for PBS Pro to integrate license aware scheduling.

## Usage

Modify the script to add the full path to **lmutil** and use it inside pbs_sched.config with

```
lmparser.py -f feature_name -c port@licserver
```
