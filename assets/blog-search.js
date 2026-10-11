/* Lightweight site.posts search; JSON is requested only after opening the dialog. */
(function () {
  "use strict";
  var button=document.getElementById("smart-search-trigger");
  var modal=document.getElementById("smart-search");
  if(!button||!modal)return;
  var input=document.getElementById("smart-search-input");
  var status=document.getElementById("smart-search-status");
  var output=document.getElementById("smart-search-results");
  var posts=null,pending=null,returnFocus=null;
  function en(){return document.documentElement.getAttribute("data-ui-lang")==="en";}
  function label(zh,english){return en()?english:zh;}
  function normalized(v){
    var s=String(v==null?"":v);
    if(s.normalize)s=s.normalize("NFKC");
    return s.toLowerCase().trim();
  }
  function item(name,cls,value){
    var node=document.createElement(name);
    if(cls)node.className=cls;
    node.textContent=value;
    return node;
  }
  function showMessage(message){status.textContent=message;}
  function render(){
    if(modal.hidden||!posts)return;
    var query=normalized(input.value),terms=query.split(/\s+/).filter(Boolean);
    output.replaceChildren();
    if(!posts.length){
      showMessage(label("目前没有已发布的博客文章。请先浏览下方专题指南。","No published blog articles yet. Explore the topic guides below."));
      return;
    }
    if(!terms.length){
      showMessage(label("已发布 "+posts.length+" 篇文章，请输入关键词。",posts.length+" published articles. Enter a keyword."));
      return;
    }
    var matches=posts.map(function(p){
      var title=normalized(p.title),keyword=normalized(p.keyword),desc=normalized(p.description);
      var headings=normalized(Array.isArray(p.headings)?p.headings.join(" "):"");
      var score=0;
      for(var i=0;i<terms.length;i++){
        var q=terms[i],weight=0;
        if(title.indexOf(q)!==-1)weight+=12;
        if(keyword.indexOf(q)!==-1)weight+=10;
        if(headings.indexOf(q)!==-1)weight+=7;
        if(desc.indexOf(q)!==-1)weight+=4;
        if(!weight)return null;
        score+=weight;
      }
      return {post:p,score:score};
    }).filter(Boolean).sort(function(a,b){return b.score-a.score;}).slice(0,30);
    showMessage(matches.length
      ?label("找到 "+matches.length+" 篇相关文章"+(matches.length===30?"（最多显示30篇）":"")+".",
             matches.length+" matching articles"+(matches.length===30?" (top 30 shown)":"")+".")
      :label("没有匹配的已发布文章。请尝试其它关键词。","No published articles match. Try another keyword."));
    matches.forEach(function(result){
      var p=result.post;
      if(!/^\/blog\/[^?#]+\/?$/.test(String(p.url||"")))return;
      var a=document.createElement("a");
      a.className="smart-search-result";
      a.href=p.url;
      a.appendChild(item("strong","smart-search-result-title",p.title||""));
      a.appendChild(item("span","smart-search-result-topic",p.topic||""));
      if(p.description)a.appendChild(item("span","smart-search-result-description",p.description));
      output.appendChild(a);
    });
  }
  function load(){
    if(pending)return pending;
    pending=fetch("/assets/search/posts.json",{credentials:"same-origin"})
      .then(function(response){if(!response.ok)throw Error("HTTP "+response.status);return response.json();})
      .then(function(data){
        if(!Array.isArray(data))throw Error("Index is not a list");
        posts=data.filter(function(p){return p&&typeof p.url==="string"&&typeof p.title==="string";});
        render();
      })
      .catch(function(){
        pending=null;
        if(!modal.hidden)showMessage(label("无法读取搜索数据，请稍后重试。","Could not load the search index. Please try again."));
      });
    return pending;
  }
  function close(){
    if(modal.hidden)return;
    modal.hidden=true;
    document.body.classList.remove("smart-search-open");
    button.setAttribute("aria-expanded","false");
    if(returnFocus&&typeof returnFocus.focus==="function")returnFocus.focus();
  }
  function open(){
    if(!modal.hidden)return;
    var menu=document.getElementById("main-nav"),menuButton=document.getElementById("menu-toggle");
    if(menu&&menu.classList.contains("mobile-open")&&menuButton)menuButton.click();
    returnFocus=document.activeElement;
    modal.hidden=false;
    document.body.classList.add("smart-search-open");
    button.setAttribute("aria-expanded","true");
    input.focus();
    if(posts)render();
    else{showMessage(label("正在载入已发布文章…","Loading published articles…"));load();}
  }
  button.addEventListener("click",open);
  modal.querySelectorAll("[data-search-close]").forEach(function(el){el.addEventListener("click",close);});
  input.addEventListener("input",render);
  document.addEventListener("keydown",function(e){
    if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==="k"){
      e.preventDefault();modal.hidden?open():close();return;
    }
    if(modal.hidden)return;
    if(e.key==="Escape"){e.preventDefault();close();return;}
    if(e.key==="Tab"){
      var tabbables=[input].concat(Array.prototype.slice.call(modal.querySelectorAll("button,a[href]")));
      var first=tabbables[0],last=tabbables[tabbables.length-1];
      if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}
      else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}
    }
  });
})();