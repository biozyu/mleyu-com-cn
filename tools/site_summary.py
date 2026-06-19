import json
from typing import Dict, List, Optional

def load_site_data() -> List[Dict[str, object]]:
    """获取内置站点资料数据集"""
    sites = [
        {
            "name": "乐鱼体育",
            "url": "https://mleyu.com.cn",
            "tags": ["体育", "娱乐", "直播", "互动"],
            "description": "乐鱼体育是一家专注于体育赛事直播与互动娱乐的平台，提供丰富的体育内容和实时赛况。",
            "keywords": ["乐鱼体育", "体育直播", "赛事资讯", "运动社区"]
        },
        {
            "name": "知识星球",
            "url": "https://zsxq.com",
            "tags": ["知识", "社区", "付费", "专栏"],
            "description": "知识星球是一个连接创作者与粉丝的付费知识社区平台。",
            "keywords": ["知识付费", "社群", "专栏", "内容变现"]
        },
        {
            "name": "GitHub",
            "url": "https://github.com",
            "tags": ["代码", "开源", "协作", "版本控制"],
            "description": "全球最大的代码托管平台，支持开源项目协作与版本控制。",
            "keywords": ["开源", "代码仓库", "Git", "协作开发"]
        }
    ]
    return sites

def format_site_entry(site: Dict[str, object], index: int) -> str:
    """将单个站点格式化为结构化摘要行"""
    name = site.get("name", "未知站点")
    url = site.get("url", "")
    tags = site.get("tags", [])
    keywords = site.get("keywords", [])
    desc = site.get("description", "")
    
    tag_str = ", ".join(tags)
    kw_str = ", ".join(keywords)
    
    lines = [
        f"站点 {index}: {name}",
        f"  URL: {url}",
        f"  标签: {tag_str}",
        f"  关键词: {kw_str}",
        f"  简介: {desc}",
        f"{'-' * 40}"
    ]
    return "\n".join(lines)

def generate_summary(sites: Optional[List[Dict[str, object]]] = None) -> str:
    """生成站点资料的结构化摘要字符串"""
    if sites is None:
        sites = load_site_data()
    
    header = "=== 内置站点资料结构化摘要 ==="
    separator = "=" * 40
    summary_parts = [header, separator]
    
    for idx, site in enumerate(sites, start=1):
        summary_parts.append(format_site_entry(site, idx))
    
    footer = f"共收录 {len(sites)} 个站点"
    summary_parts.append(footer)
    
    return "\n".join(summary_parts)

def main():
    """主入口：输出站点摘要"""
    summary = generate_summary()
    print(summary)

if __name__ == "__main__":
    main()