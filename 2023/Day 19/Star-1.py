import re

workflows, parts = open('input', 'r').read().split('\n\n')
workflow_rules = {}
for workflow in workflows.split():
    workflow_rules[workflow[:workflow.find('{')]] = []
    for rule in workflow[workflow.find('{') + 1:-1].split(','):
        if ':' in rule:
            workflow_rules[workflow[:workflow.find('{')]].append(rule.split(':'))
        else:
            workflow_rules[workflow[:workflow.find('{')]].append(('True', rule))
summate = 0
for part in parts.split():
    cur, (x, m, a, s) = 'in', list(map(int, re.findall(r'\d+', part)))
    while cur not in 'AR':
        for rule in workflow_rules[cur]:
            if eval(rule[0]):
                cur = rule[1]
                break
    if cur == 'A':
        summate += x + m + a + s
print(summate)
