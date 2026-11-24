# pairwise-morph-target-blend

## 领域

游戏、图形与多媒体

## 主题

形态目标混合

## 说明

权重统一归一、上传完成绘制与 LOD 映射。

初始状态下 `graphics/morph_target_blend.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
