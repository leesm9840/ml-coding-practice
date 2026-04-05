# -*- coding: utf-8 -*-

# �ú� ���̺귯�� �ҷ�����
import seaborn as sns

# **��(tips) �����ͼ� �ҷ�����**
tips = sns.load_dataset('tips')
print(tips.head())

tips.info()

# **������ ���� ������ �׷���**

import matplotlib.pyplot as plt

# figure�� 2���� ���� �÷��� ����
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# stripplot( ) �׸���
sns.stripplot(x='day', y='tip', hue='sex', data=tips, alpha=0.7, ax=ax1)

# swarmplot( ) �׸���
sns.swarmplot(x='day', y='tip', hue='sex', data=tips, palette='Set2', alpha=0.7, ax=ax2)

# ���� �÷��� ���� ����
ax1.set_title('Strip Plot of Tip by Day and Gender')
ax2.set_title('Swarm Plot of Tip by Day and Gender')
plt.savefig('./week04/Seaborn_Figure01.jpg')

# **�� �׷���**
# figure�� 2���� ���� �÷��� ����
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2 ,1)
ax2 = fig.add_subplot(1, 2, 2)

# �Ļ簡 �̷���� �ð��� �ľ�
# x�� ����, �����ͼ�, axe ��ü(1��° �׸���)
sns.countplot(x='time', data=tips, ax=ax1)

ax1.set_title('Frequency of Tips by Time')
ax2.set_title('Frequency of Tips by Time and Day')
plt.savefig('./week04/Seaborn_Figure02.jpg')

# **���� ȸ�ͼ� �ִ� ������**
# figure�� 2���� ���� �÷��� ����
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# �������� ���� ȸ�ͼ� ǥ��(fit_reg=True)
sns.regplot(x='total_bill', y='tip', data=tips, color='blue', scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'linestyle': '--'}, ax=ax1)

# �������� ���� ȸ�ͼ� ��ǥ��(fit_reg=False)
sns.regplot(x='total_bill', y='tip', data=tips, color='blue', scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'linestyle': '--'}, ax=ax1)

fig.suptitle('Scatter Plots with Regression Lines', fontsize=16)
ax1.set_title('fit_reg = True')
ax2.set_title('fit_reg = False')
plt.savefig('./week04/Seabotn_Figure03.jpg')

# **������׷��� Ŀ�� �е� ���� �׷���**
# ������׷��� Ŀ�� �е� ���� �׷��� �Բ� �׸���
sns.histplot(tips['tip'], bins=30, kde=True, color='skyblue')

plt.title('Histogram with KED for Tips')
plt.savefig('./week04/Seaborn_Figure05.jpg')

# **조인트 그래프**
# jointplot( ) 그리기
sns.jointplot(x='size', y='tip', data=tips, kind='scatter')

