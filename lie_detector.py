#!/usr/bin/env python3
"""
专业图像测谎工具
基于面部表情和微表情分析
"""

import sys
import os
from pathlib import Path
import requests
import json
import base64


def analyze_deception(image_path: str, model_name: str = "gemma3:12b"):
    """专门的说谎检测分析"""
    try:
        # 读取并编码图像
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        
        # 专业的说谎检测提示词
        prompt = """作为一名专业的微表情分析师和心理学家，请仔细分析这张图片中人物的面部表情，重点关注说谎和欺骗的迹象,用中文输出。

请从以下几个维度进行专业分析：

1. 眼部分析：
   - 眼神接触程度
   - 眨眼频率异常
   - 瞳孔变化
   - 眼部肌肉紧张

2. 面部微表情：
   - 表情持续时间异常（过短或过长）
   - 表情不对称
   - 强制性微笑
   - 面部肌肉紧张

3. 身体语言：
   - 面部朝向
   - 头部姿态
   - 整体紧张程度

4. 情绪一致性：
   - 表情与预期情绪的一致性
   - 多重情绪冲突

请以JSON格式返回详细分析结果：
{
  "overall_assessment": {
    "lie_probability": 0.0-1.0,
    "truthfulness_score": 1-10,
    "confidence_level": 0.0-1.0,
    "overall_impression": "整体印象描述"
  },
  "detailed_analysis": {
    "eye_analysis": {
      "eye_contact": "眼神接触分析",
      "blink_pattern": "眨眼模式分析", 
      "pupil_response": "瞳孔反应分析",
      "eye_tension": "眼部紧张度分析"
    },
    "facial_microexpressions": {
      "expression_duration": "表情持续时间分析",
      "facial_symmetry": "面部对称性分析",
      "forced_expressions": "强制表情分析",
      "muscle_tension": "肌肉紧张分析"
    },
    "body_language": {
      "head_position": "头部位置分析",
      "facial_orientation": "面部朝向分析",
      "general_tension": "整体紧张度分析"
    },
    "emotional_consistency": {
      "expression_match": "表情匹配度分析",
      "emotional_conflicts": "情绪冲突分析"
    }
  },
  "deception_indicators": [
    "具体的欺骗指标列表"
  ],
  "truthfulness_indicators": [
    "具体的真实性指标列表"
  ],
  "professional_conclusion": "专业结论和建议",
  "limitations": "分析局限性说明"
}"""

        # 构建请求
        payload = {
            "model": model_name,
            "prompt": prompt,
            "images": [base64_image],
            "stream": False,
            "options": {
                "temperature": 0.1,  # 更低的温度以获得更一致的分析
                "num_predict": 2000  # 更多的输出用于详细分析
            }
        }
        
        # 发送请求
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=90
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result.get('response', '')
            
            # 尝试解析JSON
            try:
                if '```json' in content:
                    json_start = content.find('```json') + 7
                    json_end = content.find('```', json_start)
                    json_content = content[json_start:json_end].strip()
                elif '{' in content and '}' in content:
                    json_start = content.find('{')
                    json_end = content.rfind('}') + 1
                    json_content = content[json_start:json_end]
                else:
                    json_content = content
                
                analysis = json.loads(json_content)
                return {"success": True, "analysis": analysis, "raw": content}
            except:
                return {"success": True, "analysis": {"raw_text": content}, "raw": content}
        else:
            return {"success": False, "error": f"API错误: {response.status_code}"}
            
    except Exception as e:
        return {"success": False, "error": str(e)}


def display_deception_analysis(analysis):
    """显示说谎检测分析结果"""
    if "raw_text" in analysis:
        print("📄 分析结果:")
        print(analysis["raw_text"])
        return
    
    # 显示整体评估
    overall = analysis.get("overall_assessment", {})
    print("🎯 整体评估:")
    print(f"   🎲 说谎可能性: {overall.get('lie_probability', 0):.2f} (0=诚实, 1=说谎)")
    print(f"   ✅ 真实性评分: {overall.get('truthfulness_score', 0)}/10")
    print(f"   🔍 分析置信度: {overall.get('confidence_level', 0):.2f}")
    print(f"   💭 整体印象: {overall.get('overall_impression', '')}")
    
    # 显示详细分析
    detailed = analysis.get("detailed_analysis", {})
    if detailed:
        print("\n🔬 详细分析:")
        
        # 眼部分析
        eye_analysis = detailed.get("eye_analysis", {})
        if eye_analysis:
            print("   👁️  眼部分析:")
            for key, value in eye_analysis.items():
                if value:
                    print(f"      • {value}")
        
        # 面部微表情
        facial = detailed.get("facial_microexpressions", {})
        if facial:
            print("   😐 面部微表情:")
            for key, value in facial.items():
                if value:
                    print(f"      • {value}")
        
        # 身体语言
        body = detailed.get("body_language", {})
        if body:
            print("   🤸 身体语言:")
            for key, value in body.items():
                if value:
                    print(f"      • {value}")
        
        # 情绪一致性
        emotional = detailed.get("emotional_consistency", {})
        if emotional:
            print("   💫 情绪一致性:")
            for key, value in emotional.items():
                if value:
                    print(f"      • {value}")
    
    # 显示指标
    deception_indicators = analysis.get("deception_indicators", [])
    if deception_indicators:
        print("\n⚠️  欺骗指标:")
        for indicator in deception_indicators:
            print(f"   • {indicator}")
    
    truthfulness_indicators = analysis.get("truthfulness_indicators", [])
    if truthfulness_indicators:
        print("\n✅ 真实性指标:")
        for indicator in truthfulness_indicators:
            print(f"   • {indicator}")
    
    # 专业结论
    conclusion = analysis.get("professional_conclusion", "")
    if conclusion:
        print(f"\n🎓 专业结论:")
        print(f"   {conclusion}")
    
    # 局限性说明
    limitations = analysis.get("limitations", "")
    if limitations:
        print(f"\n⚠️  分析局限性:")
        print(f"   {limitations}")


def main():
    """主函数"""
    print("🕵️ 专业说谎检测工具")
    print("=" * 60)
    
    # 检查参数
    if len(sys.argv) < 2:
        print("用法: python lie_detector.py <图像路径> [模型名称]")
        print("示例: python lie_detector.py person.jpg")
        print("示例: python lie_detector.py person.jpg gemma3:12b")
        sys.exit(1)
    
    image_path = sys.argv[1]
    model_name = sys.argv[2] if len(sys.argv) > 2 else "gemma3:12b"
    
    if not Path(image_path).exists():
        print(f"❌ 图像文件不存在: {image_path}")
        sys.exit(1)
    
    print(f"🖼️  分析图像: {Path(image_path).name}")
    print(f"🤖 使用模型: {model_name}")
    print("=" * 60)
    print("🔍 正在进行专业说谎检测分析...")
    print("⏳ 这可能需要一些时间，请耐心等待...")
    
    # 执行分析
    result = analyze_deception(image_path, model_name)
    
    if result["success"]:
        print("\n" + "=" * 60)
        display_deception_analysis(result["analysis"])
        print("\n" + "=" * 60)
        print("✅ 专业分析完成！")
        print("\n💡 注意: 此分析仅供参考，不能作为法律或医学诊断依据")
    else:
        print(f"❌ 分析失败: {result['error']}")


if __name__ == "__main__":
    main()