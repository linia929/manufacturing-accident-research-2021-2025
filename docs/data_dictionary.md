# 字段说明

case_id：稳定事故编号；L轻工纺织、M冶金、N有色金属制造活动。数字是研究顺序，不是官方事故编号，也不连续补号。

cases_103.csv保留行业、年份、地区、报告题名、既有中国研究主类、作业任务、官方网址。research_type_GB不等于ESAW接触方式。

international_axis_103.csv每行一份事故报告的接触摘要：
- ESAW2013_contact_code：必须按文本读取，保留00；不是空值或数字0。
- decision_resolution：specific细码、group_only仅组级、not_unique不能唯一确定。三者都已有逐案理由，不是处理进度标签。
- evidence_based_reason：研究判断与依据概述，不冒充原文引号。
- alternative_codes：候选或敏感性码，用竖线分隔，不参与主码计数；候选不是第二个确定主码。
- non_unique_kind：区分同案死亡者接触不同、同一伤者严重性无法排序、接触细节缺失；事故级00不等于全部受害者都没有信息。
- report_section/evidence_locator：查原报告的章节与定位；文字提取行号依赖证据文本版本。扫描件用PDF页与印刷页，内部保存图像核对记录。
- official_url/supplement_url：官方报告入口与补充证据；L62的介质信息来自补充案例，不伪称原报告鉴定。
- coding_unit/unit_scope_note：事故级主接触摘要及选取范围，不等同于完整的受伤者级ESAW记录。
- evidence_text_sha256：内部所用证据提取文本的SHA256，便于固定版本；内部文本不随此包分发。

evidence_index_49.csv仅对应既有49起重点组的H人、M机器、E环境、G管理原因证据定位；1=有肯定原因记录，0=该表无肯定记录，不是证明没有该原因。它与103起接触编码是不同任务。

esaw_counts.csv：事故级接触摘要计数。share_all_103分母103含00；share_among_90_assignable仅用于可判定记录内部构成，00留空。均为比例0—1，不是全国发生率。

esaw_victim_groups_selected.csv：只保留六组报告明确叙述的受害者群组。group_id是分组编号，不是个人身份；不得把六组表称为完整受害者数据库，也不得与事故级行混加。

esaw_codebook_used.csv：本次实际使用代码的研究释义和官方方法指向，不再分发整套标准全文。

nonferrous_scope_13.csv是实际活动及ISIC适用性核查，不是13家企业已获正式ISIC认证。
classification_decisions.csv保存既有中国研究分类裁决，不随ESAW新轴静默覆盖。
