import re

workflows, parts = open('input', 'r').read().split('\n\n')
workflow_rules = {}
for workflow in workflows.split():
    workflow_rules[workflow[:workflow.find('{')]] = []
    for rule in workflow[workflow.find('{') + 1:-1].split(','):
        if ':' in rule:
            workflow_rules[workflow[:workflow.find('{')]].append(rule.split(':'))
        else:
            workflow_rules[workflow[:workflow.find('{')]].append(rule)


def count(cur, ranges):
    global workflow_rules
    if cur == 'A':
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    if cur == 'R':
        return 0
    summate = 0
    for i in range(len(workflow_rules[cur]) - 1):
        workflow_rule, destination = workflow_rules[cur][i]
        (lo, hi), go, stay = ranges[workflow_rule[0]], None, None
        if '<' in workflow_rule:
            go = (lo, min(int(workflow_rule[2:]) - 1, hi))
            stay = (max(int(workflow_rule[2:]), lo), hi)
        else:
            go = (max(int(workflow_rule[2:]) + 1, lo), hi)
            stay = (lo, min(int(workflow_rule[2:]), hi))
        if go[0] <= go[1]:
            new = ranges.copy()
            new[workflow_rule[0]] = go
            summate += count(destination, new)
        if stay[0] <= stay[1]:
            ranges[workflow_rule[0]] = stay
        else:
            break
    else:
        summate += count(workflow_rules[cur][-1], ranges)
    return summate


print(count('in', {ch: (1, 4000) for ch in 'xmas'}))
