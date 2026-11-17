def flatten_outline(outline, page_lookup, depth=0):
    rows=[]
    for item in outline:
        if isinstance(item,list):
            rows.extend(flatten_outline(item,page_lookup,depth+1))
            continue
        title=str(getattr(item,"title","Untitled"))
        try: page=page_lookup(item)
        except Exception: page=None
        rows.append({"title":title,"page":page+1 if isinstance(page,int) else None,"depth":depth})
    return rows

def to_markdown(items,title):
    lines=[f"# {title}",""]
    for item in items:
        suffix=f" (p. {item['page']})" if item["page"] else " (page unavailable)"
        lines.append("  "*item["depth"]+f"- {item['title']}{suffix}")
    return "\n".join(lines)
