/* Quick Call and local site chatbot for CHINA.
   Adapted from the interaction model in thuexemayhanoi/french/assets/js/assistant.js.
   No AI API, external chat service, cookies or user-question upload. */
(function () {
  "use strict";
  var translations={
    zh:{quick:"快捷联系",call:"拨打电话",zalo:"Zalo 咨询",whatsapp:"WhatsApp 联系",map:"查看地图",assistant:"租车助手",subtitle:"本地问答 · 无需 AI API",close:"关闭聊天",send:"发送",placeholder:"咨询河内租车、押金或车型…",question:"租车问题",greet:"您好！我是 Nguyễn Tú 网站的本地问答助手，根据本站公开的车型、价格和常见问题回答。不能实时查询库存、确认预订或提供法律保证。",loading:"正在查询本站资料…",unavailable:"当前无法读取本站问答索引。您可以通过电话或 Zalo 联系门店确认。",fallback:"本站目前没有足够信息准确回答这个问题。请查看相关页面，或联系门店确认。",contact:"联系门店",source:"查看网站资料 →",rate:"参考租金",deposit:"参考押金（另计）",confirm:"价格及押金以门店确认和租赁合同为准。",unknown:"该车型和租期未公布统一价格，请向门店询价。",available:"无法实时查询车辆库存或自动确认预订。请联系门店说明车型和日期。",licence:"50cc 或其他车型的驾驶资格、年龄及证件要求应以越南现行法规和实际车辆类别为准，不能默认不需要驾照。",delivery:"老城区配送、异地交接、时间和可能产生的费用均需先向门店核实；门店位于龙编区，不在老城区内。",periodDaily:"每天",periodWeekly:"每周",periodMonthly:"每月",hours:"营业时间",address:"门店地址",phone:"电话",promptPrice:"50cc 价格",promptDeposit:"押金",promptAddress:"门店地址",promptHours:"营业时间",promptRules:"骑行规定",promptContact:"联系",generalPrice:"常见车型参考日租 150,000–200,000 VND，押金按车型另计。不同车型与租期请查看价格表。",faqIntro:"根据本站常见问题：",disclaimer:"本站信息仅供参考，签约前请核实实际费用和条件。"},
    en:{quick:"Quick Contact",call:"Call Now",zalo:"Message on Zalo",whatsapp:"WhatsApp",map:"Open Map",assistant:"Rental Assistant",subtitle:"Local answers · no AI API",close:"Close chat",send:"Send",placeholder:"Ask about Hanoi rentals, deposits or vehicles…",question:"Rental question",greet:"Hello! I'm Nguyễn Tú's local site assistant. I answer from published rental prices and FAQs. I cannot check live availability, confirm bookings or guarantee legal requirements.",loading:"Checking published site information…",unavailable:"The site's FAQ index is temporarily unavailable. Please call or message the shop to confirm details.",fallback:"I don't have enough verified site information to answer accurately. Please read the related page or contact the shop.",contact:"Contact the Shop",source:"Read source page →",rate:"Indicative rental",deposit:"Indicative deposit (extra)",confirm:"Prices and deposits must be confirmed by the shop and rental agreement.",unknown:"No published rate for this model and period. Please ask the shop for a quote.",available:"I cannot check live stock or confirm bookings. Contact the shop with the model and your dates.",licence:"Legal driving eligibility, age and document requirements for 50cc and other vehicles depend on current Vietnamese law and the actual vehicle classification. Do not assume a licence exemption.",delivery:"Old Quarter delivery, off-site handover, timing and any fees require direct confirmation. The shop is in Long Biên, not inside the Old Quarter.",periodDaily:"per day",periodWeekly:"per week",periodMonthly:"per month",hours:"Opening hours",address:"Shop address",phone:"Phone",promptPrice:"50cc Price",promptDeposit:"Deposit",promptAddress:"Address",promptHours:"Hours",promptRules:"Driving Rules",promptContact:"Contact",generalPrice:"Indicative daily rates for common models are VND 150,000–200,000. Deposits are separate and depend on the vehicle. Check the price table for model details.",faqIntro:"From our published FAQ:",disclaimer:"This information is indicative. Confirm prices and terms before renting."}
  };
  function lang(){try{return window.chinaLanguage && window.chinaLanguage.get() === "en" ? "en" : document.documentElement.dataset.uiLang==="en"?"en":"zh";}catch(e){return "zh";}}
  function L(key){return translations[lang()][key]||key;}
  function escapeHTML(s){return String(s||"").replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];});}
  function icon(type){
    var paths={
      phone:'<path d="M21 16.5v3a1.5 1.5 0 0 1-1.7 1.5A18.5 18.5 0 0 1 3 4.7 1.5 1.5 0 0 1 4.5 3h3A1.5 1.5 0 0 1 9 4.3c.1 1 .4 2 .7 2.9a1.5 1.5 0 0 1-.3 1.6L8 10.2a15 15 0 0 0 5.8 5.8l1.4-1.4a1.5 1.5 0 0 1 1.6-.3c.9.3 1.9.6 2.9.7a1.5 1.5 0 0 1 1.3 1.5z"/>',
      chat:'<path d="M21 12a8.5 8.5 0 0 1-12.4 7.5L4 21l1.6-4.4A8.5 8.5 0 1 1 21 12z"/><path d="M9 11.5h.01M12.5 11.5h.01M16 11.5h.01"/>',
      map:'<path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
      message:'<path d="M4 5.5h16v11H8l-4 3v-14z"/><path d="M8 10h8M8 13h5"/>'
    };
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+(paths[type]||"")+'</svg>';
  }
  function norm(s){return String(s||"").normalize("NFKC").toLowerCase().replace(/[，。？！、；：“”‘’()\[\]{}.,!?;:\-_/\\]/g," ").replace(/\s+/g," ").trim();}
  function money(n){return new Intl.NumberFormat("en-US").format(n)+" VND";}
  function range(value){if(!Array.isArray(value))return null;return value[0]===value[1]?money(value[0]):money(value[0])+" – "+money(value[1]);}
  function depositText(v){
    var s=String(v&&v.deposit||"");
    if(lang()==="en")return s.replace(/(\d+(?:–\d+)?)\s*百万 ₫/g,"$1 million VND").replace("按车型确认","Ask the shop");
    return s;
  }
  function sourceUrl(url){
    if(!/^\/(?!\/)/.test(url||""))return "/contact/";
    return url;
  }
  function matches(q,pattern){return pattern.test(q);}
  function vehicleMatch(q,data){
    var models=(data&&data.vehicles)||[];
    return models.find(function(v){
      var n=String(v.name).toLowerCase();
      if(/50\s*cc/.test(q))return /50cc/.test(n);
      if(/vision/.test(q))return /vision/.test(n);
      if(/air\s*blade/.test(q))return /air blade/.test(n);
      if(/wave/.test(q))return /wave/.test(n);
      if(/click|mio/.test(q))return /click|mio/.test(n);
      if(/electric|e-bike|电动|電動/.test(q))return /电动/.test(n);
      return false;
    });
  }
  function matchScore(query,text){
    var q=norm(query),t=norm(text);
    if(!q||!t)return 0;
    if(t.indexOf(q)!==-1&&q.length>3)return 18;
    var latin=q.match(/[a-z\d]{3,}/g)||[];
    var han=q.match(/[\u3400-\u9fff]+/g)||[];
    var terms=latin.concat(han.filter(function(x){return x.length>=2;}));
    han.forEach(function(chunk){for(var i=0;i+2<=chunk.length;i++)terms.push(chunk.slice(i,i+2));});
    var seen={},score=0;
    terms.forEach(function(term){if(seen[term])return;seen[term]=true;if(t.indexOf(term)!==-1)score+=term.length>3?4:2;});
    return score;
  }
  var indexPromise=null;
  function loadIndex(){
    if(indexPromise)return indexPromise;
    indexPromise=fetch("/assets/chat/site-index.json?v=1",{cache:"default"})
      .then(function(response){if(!response.ok)throw Error("site-index");return response.json();})
      .then(function(d){if(!d||!Array.isArray(d.faqs)||!Array.isArray(d.pages)||!Array.isArray(d.vehicles))throw Error("invalid site-index");return d;})
      .catch(function(){return null;});
    return indexPromise;
  }
  function getAnswer(question,data){
    var q=norm(question),en=lang()==="en",b=data.business||{},model=vehicleMatch(q,data);
    var price=matches(q,/多少钱|价格|价钱|费用|报价|租金|收费|cost|price|rate|how much|daily rate|weekly rate|monthly rate|per day|per week|per month/);
    var deposit=matches(q,/押金|保证金|抵押|deposit|security|caution/);
    var legal=matches(q,/驾照|驾驶证|许可证|需要.*证|法[律规]|合[法规]|年龄|无证|license|licence|permit|legal|driv.*rule|driv.*age|no licence/);
    var stock=matches(q,/库存|有车|现在有|还有车|现货|预订|预定|订车|book|reserv|available|availability|stock|in stock/);
    var delivery=matches(q,/配送|送车|送到|上门|交接地点|delivery|deliver|pickup|pick.up|drop.off/);
    var addr=matches(q,/地址|在哪里|在哪儿|定位|怎么走|地图|位置|地点|where|address|location|direction|map|old quarter|老城区|古街|旧城区/);
    var hours=matches(q,/几点|开门|关门|营业|工作时间|hours|opening|closing|open today|close today/);
    var contact=matches(q,/电话|联系|zalo|whatsapp|客服|热线|call|contact|phone|message/);
    if(stock)return {text:L("available"),url:"/contact/"};
    if(legal)return {text:L("licence"),url:"/topics/50cc/requirements/"};
    if(delivery)return {text:L("delivery"),url:"/topics/old-quarter/pickup/"};
    if(hours)return {text:L("hours")+": "+String(b.opens||"09:00")+"–"+String(b.closes||"21:00")+" (Hanoi).",url:"/contact/"};
    if(addr)return {text:L("address")+": "+String(b.address||"112 Nguyễn Văn Cừ, Bồ Đề, Long Biên, Hà Nội")+".",url:"/contact/"};
    if(contact)return {text:L("phone")+": "+String(b.phone_display||"+84 942 467 674")+". Zalo / WhatsApp.",url:"/contact/"};
    if(deposit){
      if(model)return {text:L("deposit")+": "+depositText(model)+". "+L("confirm"),url:"/prices/"};
      return {text:(en?"Deposits generally range from 2–5 million VND, depending on the model. ":"押金一般为 2–5 百万越南盾，按车型确定。")+L("confirm"),url:"/topics/pricing/deposits/"};
    }
    if(price||model){
      if(model){
        var unit=matches(q,/month|monthly|月租|每月|一个月|1个月/ )?"month":matches(q,/week|weekly|周租|每周|一周/)?"week":"day";
        var amount=range(model[unit]);
        var name=model.name;if(en)name=name.replace("踏板车","Scooter").replace("电动摩托车 / 电动自行车","Electric Motorbike / E-bike");
        var per=unit==="month"?L("periodMonthly"):unit==="week"?L("periodWeekly"):L("periodDaily");
        return {text:amount?name+" — "+L("rate")+" "+per+": "+amount+". "+L("deposit")+": "+depositText(model)+". "+L("confirm"):L("unknown"),url:"/prices/"};
      }
      return {text:L("generalPrice")+" "+L("confirm"),url:"/prices/"};
    }
    // Published FAQ answers are preferred over invented content.
    var bestFAQ=null,max=0;
    data.faqs.forEach(function(f){
      var fields=en?String(f.englishQuestion||f.question):String(f.question);
      var s=matchScore(q,fields);
      if(s>max){max=s;bestFAQ=f;}
    });
    if(bestFAQ&&max>=6)return {text:L("faqIntro")+" "+String(en?(bestFAQ.englishAnswer||bestFAQ.answer):bestFAQ.answer),url:"/faq/"};
    var bestPage=null,top=0;
    data.pages.forEach(function(p){
      var s=matchScore(q,String(p.title||"")+" "+String(p.description||""));
      if(s>top){top=s;bestPage=p;}
    });
    if(bestPage&&top>=7)return {text:L("fallback"),url:sourceUrl(bestPage.url)};
    return {text:L("fallback"),url:"/contact/"};
  }
  function mount(){
    if(document.getElementById("china-quick")||document.getElementById("china-chat-fab"))return;
    var configTag=document.getElementById("china-assistant-config");
    if(!configTag)return;
    var cfg;try{cfg=JSON.parse(configTag.textContent);}catch(e){return;}
    var feature=cfg.features||{},business=cfg.business||{};
    if(!feature.quick_contact&&!feature.local_chatbot)return;
    var phone=String(business.phone_e164||""), quick=null, main=null, fab=null, panel=null, textInput=null,log=null;
    if(feature.quick_contact){
      quick=document.createElement("div");quick.id="china-quick";quick.className="china-quick";quick.dataset.open="false";quick.setAttribute("translate","no");
      var actions=[
        {url:"tel:"+phone,key:"call",icon:"phone",target:false},
        {url:business.zalo,key:"zalo",icon:"message",target:true},
        {url:business.whatsapp,key:"whatsapp",icon:"message",target:true},
        {url:business.maps,key:"map",icon:"map",target:true}
      ].filter(function(a){return !!a.url && a.url!=="tel:";});
      quick.innerHTML='<button class="china-quick-main" type="button" aria-expanded="false" aria-controls="china-quick-actions" data-ui-label="quick">'+icon("phone")+'</button><div class="china-quick-actions" id="china-quick-actions">'+actions.map(function(a){return '<a class="china-quick-action" href="'+escapeHTML(a.url)+'"'+(a.target?' target="_blank" rel="noopener noreferrer"':'')+' data-ui-label="'+a.key+'">'+icon(a.icon)+'<span class="china-quick-tip" data-ui="'+a.key+'"></span></a>';}).join("")+'</div>';
      document.body.appendChild(quick);main=quick.querySelector(".china-quick-main");
    }
    if(feature.local_chatbot){
      fab=document.createElement("button");fab.type="button";fab.id="china-chat-fab";fab.className="china-chat-fab";fab.setAttribute("aria-expanded","false");fab.setAttribute("aria-controls","china-chat-panel");fab.setAttribute("translate","no");fab.innerHTML=icon("chat")+'<span class="china-chat-tip" data-ui="assistant"></span>';document.body.appendChild(fab);
      panel=document.createElement("section");panel.id="china-chat-panel";panel.className="china-chat-panel";panel.hidden=true;panel.setAttribute("role","dialog");panel.setAttribute("aria-modal","false");panel.setAttribute("translate","no");
      panel.innerHTML='<div class="china-chat-head"><div><strong class="china-chat-title" data-ui="assistant"></strong><span class="china-chat-subtitle" data-ui="subtitle"></span></div><button class="china-chat-close" type="button" data-ui-label="close">×</button></div><div class="china-chat-log" role="log" aria-live="polite" aria-relevant="additions"></div><div class="china-chat-shortcuts">'+["promptPrice","promptDeposit","promptAddress","promptHours","promptRules","promptContact"].map(function(k){return '<button type="button" data-prompt="'+k+'" data-ui="'+k+'"></button>';}).join("")+'</div><form class="china-chat-form"><input class="china-chat-input" type="text" maxlength="300" autocomplete="off" required data-ui-placeholder="placeholder" data-ui-label="question"><button class="china-chat-send" type="submit" data-ui-label="send">➜</button></form>';
      document.body.appendChild(panel);log=panel.querySelector(".china-chat-log");textInput=panel.querySelector(".china-chat-input");
    }
    function updateLabels(){
      var roots=[quick,panel,fab].filter(Boolean);
      roots.forEach(function(root){
        root.querySelectorAll("[data-ui]").forEach(function(el){el.textContent=L(el.dataset.ui);});
        root.querySelectorAll("[data-ui-label]").forEach(function(el){el.setAttribute("aria-label",L(el.dataset.uiLabel));});
        root.querySelectorAll("[data-ui-placeholder]").forEach(function(el){el.placeholder=L(el.dataset.uiPlaceholder);});
      });
      if(fab)fab.setAttribute("aria-label",L("assistant"));
      if(panel)panel.setAttribute("aria-label",L("assistant")+" Nguyễn Tú");
    }
    function setQuick(open){
      if(!quick)return;
      quick.dataset.open=String(!!open);main.setAttribute("aria-expanded",String(!!open));
    }
    function setChat(open){
      if(!panel)return;
      panel.hidden=!open;fab.setAttribute("aria-expanded",String(!!open));
      if(open){
        setQuick(false);loadIndex();
        if(!panel.dataset.greeted){panel.dataset.greeted="1";message(L("greet"),"bot");}
        if(window.innerWidth>700)setTimeout(function(){textInput.focus({preventScroll:true});},60);
      }else{
        panel.dataset.keyboardOpen="false";document.body.classList.remove("china-chat-keyboard");
        if(document.activeElement===textInput)textInput.blur();
      }
    }
    function message(value,who,url){
      if(!log)return;
      var item=document.createElement("div");item.className="china-chat-msg "+who;item.textContent=String(value||"");log.appendChild(item);
      if(url&&who==="bot"){var a=document.createElement("a");a.className="china-chat-source";a.href=sourceUrl(url);a.textContent=L("source");log.appendChild(a);}
      log.scrollTop=log.scrollHeight;
    }
    function promptValue(key){
      var en=lang()==="en";
      return {
        promptPrice:en?"What is the price of a 50cc scooter?":"50cc 踏板车一天多少钱？",
        promptDeposit:en?"How much is the deposit?":"租车押金多少钱？",
        promptAddress:en?"Where is the shop?":"门店地址在哪里？",
        promptHours:en?"What are your opening hours?":"营业时间是几点？",
        promptRules:en?"Do I need a licence for a 50cc scooter?":"50cc 需要驾照吗？",
        promptContact:en?"How can I contact the shop?":"怎么联系门店？"
      }[key]||"";
    }
    async function send(text){
      text=String(text||"").trim();
      if(!text)return;
      message(text,"user");
      var temporary=document.createElement("div");temporary.className="china-chat-msg bot";temporary.textContent=L("loading");log.appendChild(temporary);log.scrollTop=log.scrollHeight;
      var d=await loadIndex();temporary.remove();
      if(!d){message(L("unavailable"),"bot","/contact/");return;}
      var result=getAnswer(text,d);
      message(result.text,"bot",result.url);
    }
    if(main)main.addEventListener("click",function(){setChat(false);setQuick(quick.dataset.open!=="true");});
    if(fab)fab.addEventListener("click",function(){setChat(panel.hidden);});
    if(panel){
      panel.querySelector(".china-chat-close").addEventListener("click",function(){setChat(false);fab.focus({preventScroll:true});});
      panel.querySelector(".china-chat-form").addEventListener("submit",function(e){e.preventDefault();var val=textInput.value;textInput.value="";send(val);});
      panel.querySelectorAll("[data-prompt]").forEach(function(el){el.addEventListener("click",function(){send(promptValue(el.dataset.prompt));});});
    }
    document.addEventListener("click",function(e){if(quick&&quick.dataset.open==="true"&&!quick.contains(e.target))setQuick(false);});
    document.addEventListener("keydown",function(e){if(e.key==="Escape"){setQuick(false);if(panel&&!panel.hidden)setChat(false);}});
    var menu=document.getElementById("main-nav");
    if(menu){
      var navChanged=function(){var open=menu.classList.contains("mobile-open");document.body.classList.toggle("china-menu-open",open);if(open){setQuick(false);setChat(false);}};
      new MutationObserver(navChanged).observe(menu,{attributes:true,attributeFilter:["class"]});navChanged();
    }
    // Apply Chinese/English UI immediately and track the existing language toggle.
    updateLabels();
    new MutationObserver(updateLabels).observe(document.documentElement,{attributes:true,attributeFilter:["data-ui-lang"]});
    if(panel&&window.visualViewport){
      var vv=window.visualViewport;
      function viewport(){
        if(panel.hidden)return;
        var keyboard=(window.innerHeight-vv.height>150)&&document.activeElement===textInput;
        panel.dataset.keyboardOpen=String(keyboard);
        document.body.classList.toggle("china-chat-keyboard",keyboard);
        if(keyboard){
          document.documentElement.style.setProperty("--china-vv-top",Math.max(8,vv.offsetTop+8)+"px");
          document.documentElement.style.setProperty("--china-vv-height",Math.max(260,vv.height-16)+"px");
        }
      }
      vv.addEventListener("resize",viewport);vv.addEventListener("scroll",viewport);
      textInput.addEventListener("focus",function(){setTimeout(viewport,80);});
      textInput.addEventListener("blur",function(){setTimeout(viewport,80);});
    }
  }
  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",mount,{once:true});else mount();
})();