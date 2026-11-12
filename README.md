# 中国制造活动事故报告研究：2021—2025

## 范围与本版结果

103起事故的官方报告元数据及ESAW 2013接触方式研究记录。103起全部有判定依据：85起细码、5起仅组级、13起因资料不足或事故级不唯一记00；不是103起均能唯一细分。

本库将中国研究主类、工作任务、接触方式、经济活动分轴保存。国际可迁移性依靠同样的字段、判定顺序、证据定位和未知处理，而不是把中国名称改成国际名称。

ESAW以受伤者为记录对象，本版本是事故级摘要，不能直接作为完整ESAW报送数据。少数多人事故的不同接触保存在补充分组表中。数据由AI辅助整理和判定，作者需核查并对论文使用负责；未声称双人编码或专家认证。

## 文件

- data/cases_103.csv：103起基础元数据和官方链接。
- data/international_axis_103.csv：103起逐案接触判定、理由、替代码和证据定位。
- data/esaw_counts.csv：接触方式计数与明确分母的比例。
- data/esaw_codebook_used.csv：本轮实际使用代码的中文研究释义。
- data/esaw_victim_groups_selected.csv：六组已明确描述的受害者分组，不是完整名册。
- data/evidence_index_49.csv：既有49起重点组的人、机、环、管原因证据定位。
- data/classification_decisions.csv：既有中国研究分类的个案处理。
- data/nonferrous_scope_13.csv：有色组13起的实际工序与ISIC适用性。
- docs/esaw_coding_rules.md：可复用判定规则与分析单位边界。
- docs/data_dictionary.md：字段、空值与分母说明。
- scripts/reproduce_counts.py：标准库复算与103行覆盖检查。
- [reports/](reports/)：103起官方调查报告索引，首批收录84份档案文件，其余19起保留官方发布入口和待复核状态。
- MANIFEST.sha256：此版本文件完整性校验。

## 复算

在仓库根目录执行：
```powershell
python scripts/reproduce_counts.py
```

样本为能取得完整官方调查报告的研究资料，不是全国事故普查。此处比例不是行业事故率，也不代表中国所有事故或其他国家总体。

## 权利与私有审阅

本仓库供作者与导师私有审阅。官方调查报告归档另列于 [reports/](reports/)；报告来源、载体和收录状态见该目录。不上传论文稿件、会议记录、内部编码原文摘录或标准全文。第三方资料权利属于各自权利人。

未指定开源许可证。转公开需由作者确认发布许可、隐私及期刊要求；私有地址不等于所有审稿人可访问的公开数据地址。

方法原文：https://ec.europa.eu/eurostat/documents/3859598/5926181/KS-RA-12-102-EN.PDF
