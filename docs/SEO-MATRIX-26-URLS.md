# SEO Matrix — 26 URL hiện có / CHINA (zh-CN)

**Repo:** [thuexemayhanoi/china](https://github.com/thuexemayhanoi/china) · **Canonical:** https://zh.rentbikehanoi.com/  
**Baseline:** `main` @ `dad8c4845c1ed361ff70a7d2a329e76781906eeb` · audit mã nguồn 2026-10-10.  
**Phạm vi:** 26 trang hiện có; **KHÔNG** phải matrix 250 bài mới (`data/china-matrix.csv`).  
**Hạn chế kiểm chứng:** Trạng thái bên dưới dựa trên front matter, template, JSON, sitemap trong repo; **chưa** xác thực HTTP trực tiếp từng URL, GSC/Bing, crawl thực tế, PSI hay độ index của Google/Baidu. Không được báo PASS cho các mục chưa đo.
**Chủ trương:** Lập kế hoạch trước; chưa sửa nội dung HTML/SEO, chưa cài workflow SEO mới, chưa đổi deployment, CNAME hoặc DNS. Mỗi lượt tối ưu 2–5 URL và kiểm tra trước/sau.

## A. Kết quả audit tĩnh có bằng chứng

- **26 trang:** 8 trang nền tảng (home, prices, about, contact, FAQ, blog, privacy, terms); 5 danh mục cha; 13 danh mục con.
- **12 URL** nằm trong `_data/site.json → sitemap_base`. Đây là **danh sách được cấu hình đưa vào sitemap**, không phải chứng nhận đã index.
- **13 danh mục con** có `noindex: true` trong front matter, đều vắng mặt khỏi danh sách sitemap nền tảng. Chúng được để noindex trong khi nội dung còn ngắn và chưa có bài hỗ trợ. **Không được bỏ noindex hàng loạt.**
- `/blog/` được template `_layouts/default.html` xuất `noindex,follow` khi chưa có post và chưa có trong sitemap nền tảng: phù hợp giai đoạn 0 bài.
- Template chung đã phát sinh meta description, canonical tuyệt đối, OG, `lang=zh-CN`, schema `WebSite`/`LocalBusiness`/`WebPage` và breadcrumbs theo front matter; FAQ schema dùng nguồn chung ở `_data/faqs.json`. Đây là **cấu hình hiện có**, chưa xác nhận JSON-LD trên output hay rich result.
- `robots.txt` cho phép crawl và trỏ `sitemap.xml`; `sitemap.xml` lấy danh sách nền tảng cộng các post được xuất bản. **Cần kiểm tra HTTP/render thực tế**.
- Nhiều trang con có khoảng **170–215 chữ Hán trong nội dung tĩnh nguồn** (không tính thành phần Jekyll dùng chung); cần bổ sung giá trị riêng trước khi cân nhắc index.
- Bản tiếng Anh hoạt động bằng JS trên cùng URL; **ưu tiên trang HTML mặc định tiếng Trung**. Không tạo `hreflang=en` khi chưa có URL tiếng Anh riêng.

## B. Matrix triển khai theo URL

**Trạng thái:** `TODO` = chưa tối ưu; khi xử lý đổi thành `IN_PROGRESS` → `QA_PASS` hoặc `BLOCKED`. Nên cập nhật theo từng batch, không đánh dấu hoàn tất nếu chưa kiểm tra thực tế.

| ID | URL | Loại | Robots theo source | Sitemap theo source | Keyword chính (简体中文) | Ưu tiên | Hạng mục chính phải làm | Trạng thái |
|---|---|---|---|---|---|---|---|---|
| SEO-01 | `/` | Trang chủ | index,follow theo template | Trong sitemap | 河内摩托车租赁 | P0 | Tối ưu giới thiệu dịch vụ/CTA, xác thực giá và NAP; tránh trùng ý định với trang giá. | QA_PASS |
| SEO-02 | `/prices/` | Giá và chuyển đổi | index,follow theo template | Trong sitemap | 河内摩托车租赁价格表 | P0 | Làm rõ bảng giá theo ngày/tuần/tháng, khoản đặt cọc tách biệt; nguồn giá tập trung, FAQ đúng thực tế. | QA_PASS |
| SEO-03 | `/topics/rental/` | Danh mục cha | index,follow theo template | Trong sitemap | 河内摩托车租赁服务 | P0 | Làm rõ xe tay ga, số sàn, thuê dài hạn, chính sách giao nhận chỉ khi xác nhận. | TODO |
| SEO-04 | `/topics/pricing/` | Danh mục cha | index,follow theo template | Trong sitemap | 河内摩托车租金指南 | P1 | Tập trung cách so sánh giá/đặt cọc; phân biệt rõ với /prices/ là bảng giá giao dịch. | TODO |
| SEO-05 | `/topics/50cc/` | Danh mục cha | index,follow theo template | Trong sitemap | 河内50cc摩托车租赁 | P0 | Trình bày mẫu xe, chi phí, yêu cầu pháp lý kiểm chứng; không khẳng định miễn bằng lái. | TODO |
| SEO-06 | `/topics/old-quarter/` | Danh mục cha | index,follow theo template | Trong sitemap | 河内老城区附近租摩托车 | P0 | Giải thích cửa hàng ở Long Biên, không nằm trong Phố Cổ; thêm dẫn đường thực tế, điều kiện giao xe. | TODO |
| SEO-07 | `/topics/guides/` | Danh mục cha | index,follow theo template | Trong sitemap | 河内摩托车租赁指南 | P1 | Cấu trúc hướng dẫn/kiểm tra xe/an toàn và câu hỏi trước thuê, hạn chế trùng nội dung trang con. | TODO |
| SEO-08 | `/about/` | Giới thiệu | index,follow theo template | Trong sitemap | Nguyễn Tú 河内摩托车租赁店 | P1 | Entity/NAP, thông tin cửa hàng có thể kiểm chứng, liên kết Maps và bằng chứng thực tế khi có. | TODO |
| SEO-09 | `/contact/` | Liên hệ | index,follow theo template | Trong sitemap | Nguyễn Tú 河内租车联系方式 | P1 | Nổi bật địa chỉ, Zalo, điện thoại, giờ mở cửa, bản đồ; rà accessibility và mobile. | TODO |
| SEO-10 | `/faq/` | FAQ | index,follow theo template | Trong sitemap | 河内租摩托车常见问题 | P1 | Kiểm tra 12 câu FAQ và giá/đặt cọc/luật, đồng bộ JSON-LD; FAQ rich result không được bảo đảm. | TODO |
| SEO-11 | `/privacy/` | Pháp lý | index,follow theo template | Trong sitemap | Nguyễn Tú 隐私政策 | P3 | Rà soát độ đúng của mô tả dữ liệu lưu trữ, dịch vụ ngoài, liên hệ yêu cầu; duyệt chính sách. | TODO |
| SEO-12 | `/terms/` | Pháp lý | index,follow theo template | Trong sitemap | Nguyễn Tú 使用条款 | P3 | Rà soát điều kiện đặt xe, trách nhiệm/đặt cọc và tuyên bố giới hạn; duyệt pháp lý. | TODO |
| SEO-13 | `/blog/` | Hub bài viết | noindex khi 0 bài | Ngoài sitemap (0 bài) | 河内摩托车租赁中文博客 | P2 | Duy trì noindex khi 0 bài; mở index/sitemap chỉ khi có bài thật và nội dung hub hữu ích. | TODO |
| SEO-14 | `/topics/rental/scooters/` | Danh mục con | noindex: true | Ngoài sitemap | 河内踏板车租赁 | P2 | Bổ sung mẫu xe, kiểm tra xe, giá dẫn về /prices/; duyệt chất lượng trước khi mở index. | TODO |
| SEO-15 | `/topics/rental/monthly/` | Danh mục con | noindex: true | Ngoài sitemap | 河内摩托车月租 | P2 | Chi tiết khoảng giá/thời hạn/hợp đồng/chi phí đặt cọc, tránh trùng danh mục cha. | TODO |
| SEO-16 | `/topics/rental/automatic/` | Danh mục con | noindex: true | Ngoài sitemap | 河内自动挡与手动挡摩托车 | P2 | So sánh đúng các kiểu xe, phù hợp người lái, nguồn an toàn, liên kết danh mục thuê. | TODO |
| SEO-17 | `/topics/pricing/daily/` | Danh mục con | noindex: true | Ngoài sitemap | 河内摩托车日租价格 | P2 | Làm rõ mức thuê/ngày theo xe đã công bố, điều kiện tính ngày và khoản chưa bao gồm. | TODO |
| SEO-18 | `/topics/pricing/weekly/` | Danh mục con | noindex: true | Ngoài sitemap | 河内摩托车周租价格 | P2 | Giá tuần cho xe có công bố; không tự suy ra gói 50cc/xe điện; liên kết bảng giá. | TODO |
| SEO-19 | `/topics/pricing/deposits/` | Danh mục con | noindex: true | Ngoài sitemap | 河内租摩托车押金 | P2 | Bảng đặt cọc tham khảo theo mẫu, quy trình trả cọc đúng hợp đồng, nguồn công khai. | TODO |
| SEO-20 | `/topics/50cc/models/` | Danh mục con | noindex: true | Ngoài sitemap | 河内50cc踏板车车型与价格 | P2 | Giá/ngày, mức cọc và mẫu 50cc thực tế, tình trạng xe cần xác minh. | TODO |
| SEO-21 | `/topics/50cc/requirements/` | Danh mục con | noindex: true | Ngoài sitemap | 越南50cc摩托车驾驶规定 | P2 | Tài liệu quy định VN hiện hành, nguồn có ngày, tuổi/giấy phép/định nghĩa xe. | TODO |
| SEO-22 | `/topics/old-quarter/directions/` | Danh mục con | noindex: true | Ngoài sitemap | 河内老城区到Long Biên租车店路线 | P2 | Google Maps và địa chỉ đúng; không bịa thời gian di chuyển hoặc lộ trình cố định. | TODO |
| SEO-23 | `/topics/old-quarter/pickup/` | Danh mục con | noindex: true | Ngoài sitemap | 河内老城区取还摩托车咨询 | P2 | Phân biệt nhận xe tại cửa hàng và giao xe khi được xác nhận; chi phí/địa điểm phải hỏi. | TODO |
| SEO-24 | `/topics/guides/contracts/` | Danh mục con | noindex: true | Ngoài sitemap | 河内租摩托车证件与合同 | P2 | Checklist giấy tờ/hợp đồng và đặt cọc; không yêu cầu hộ chiếu nếu không có chính sách chính thức. | TODO |
| SEO-25 | `/topics/guides/safety/` | Danh mục con | noindex: true | Ngoài sitemap | 河内摩托车骑行安全 | P2 | Nguồn an toàn/pháp lý rõ; hướng dẫn kiểm tra xe và hạn chế hứa hẹn. | TODO |
| SEO-26 | `/topics/guides/returns/` | Danh mục con | noindex: true | Ngoài sitemap | 河内摩托车还车与押金退还 | P2 | Đặt điều kiện trả xe và hoàn cọc theo hợp đồng; quy trình có xác minh. | TODO |

**Lưu ý SEO:** từ khóa chỉ là ánh xạ ý định và đề xuất on-page, **chưa phải số liệu volume/ranking**. `/prices/` ưu tiên bảng giá thật, `/topics/pricing/` ưu tiên hướng dẫn hiểu giá để giảm cannibalization. `/topics/old-quarter/` không được trình bày sai rằng cửa hàng ở trong Phố Cổ.

## C. 7 trục SEO cần kiểm tra — không tạo workflow lúc này

| Trục | Công việc | Phạm vi | Mức | Điều kiện nghiệm thu |
|---|---|---|---|---|
| T1 — Technical & index | Kiểm tra HTTP 200, canonical, redirect, noindex, robots, sitemap, mobile, liên kết gãy | 26 URL / 12 URL sitemap | P0 | Không có canonical sai host; không có 404 không xử lý; trang indexable và sitemap đồng nhất theo quyết định; ghi URL kiểm tra |
| T2 — Performance & CWV | Lighthouse/PSI di động, LCP/INP/CLS, tải CSS/JS, widget Quick Call và chatbot, tránh layout shift | Home + prices + FAQ + 1 trang con trước | P1 | Có kết quả đo thực tế, đề xuất định lượng; không suy diễn tốc độ từ source |
| T3 — Schema & Entity | Soát `LocalBusiness`, `WebSite`, `BreadcrumbList`, `FAQPage`, `AboutPage`; kiểm tra NAP, cấu trúc JSON-LD | Template chung, about/contact/FAQ/prices | P1 | JSON-LD parse đúng, không tự khai thông tin thiếu kiểm chứng; chỉ FAQ thật nhận FAQ schema |
| T4 — AI Search / GEO | Câu trả lời trực tiếp trong tiếng Trung, ngữ nghĩa riêng từng trang, sự kiện có thể chứng minh, thông tin nguồn và ngày cập nhật khi phù hợp | Home, prices, 50cc, FAQ, Old Quarter | P1 | Không thêu dệt giá, giao xe, bằng lái, đánh giá; không hứa chắc AI trích dẫn |
| T5 — E-E-A-T / Local trust | Địa chỉ, số điện thoại, Zalo, Maps, ảnh xe thật nếu được cung cấp, nguồn pháp lý, tác giả/biên tập; review chính sách | About/contact/prices/50cc/privacy/terms | P1 | NAP nhất quán với thông tin doanh nghiệp; đánh dấu thông tin chưa xác nhận |
| T6 — Off-page / brand | Citation doanh nghiệp chất lượng, backlink du lịch thật, kết nối site đa ngôn ngữ khi phù hợp; kiểm tra khả năng truy cập bot Trung Quốc | Domain/GBP/ngoài repo | P3 | Nguồn uy tín và liên quan; tránh link farm/PBN/spam |
| T7 — Measurement / duy trì | Xác minh GSC/Bing Webmaster, index coverage, impressions/CTR, truy vấn thực, cannibalization; cân nhắc Baidu khi mục tiêu phù hợp | Toàn domain | P2 | Có dữ liệu thực tế trước khi ra quyết định mở index hoặc sửa thứ hạng |

## D. Thứ tự xử lý an toàn (mỗi lượt nhỏ)

| Bước | Batch | URL / phạm vi | Quy tắc |
|---|---|---|---|
| 01 | Baseline index | `/`, `/prices/`, `/faq/`, `/blog/`, `robots.txt`, `sitemap.xml` | Chỉ audit trước; phân biệt indexability với index thực |
| 02 | Money pages | `/`, `/prices/`, `/topics/rental/`, `/topics/50cc/`, `/topics/old-quarter/` | Chỉnh tối đa 2–3 URL/lượt, không đổi URL |
| 03 | Trust & entity | `/about/`, `/contact/`, `/faq/`, schema chung | Đồng bộ NAP, xác minh dữ kiện, QA schema |
| 04 | Category hubs | `/topics/pricing/`, `/topics/guides/`; kiểm tra trùng intent | Không giành keyword trang giá và trang chủ |
| 05A | Child rental/pricing | 6 URL con `rental/*`, `pricing/*` | Viết nội dung độc lập và QA rồi mới xét bỏ noindex |
| 05B | Child 50cc/Old Quarter | 4 URL con `50cc/*`, `old-quarter/*` | Xác minh luật/địa điểm; không mặc định có giao xe |
| 05C | Child guides | 3 URL con `guides/*` | Kiểm tra nguồn, nội dung, link, duplicate |
| 06 | Performance & AI | 4 trang đại diện, kiểm tra mobile/AI-readable | Đo thực tế trước khi sửa CSS/JS |
| 07 | Monitoring/authority | GSC/Bing/Baidu, links uy tín; privacy/terms rà soát | Chỉ thực hiện nếu có dữ liệu/xác minh phù hợp |

**Quy trình cho MỖI batch:** audit lỗi cụ thể → xác định root cause → sửa ở template/config chung nếu có thể → kiểm tra URL/canonical/schema/menu + mobile → commit nhỏ → xác nhận deploy → cập nhật `TODO/QA_PASS/BLOCKED` trong matrix. Không sửa thủ công 26 file nếu có thể làm từ 1 template.

## E. Ràng buộc không thay đổi

- Canonical chỉ dùng `https://zh.rentbikehanoi.com/` và URL hiện có; không chuyển sang `github.io`.
- Giữ `CNAME`, DNS, GitHub Pages branch deploy, SEO 250 bài và `/french` nguyên vẹn.
- Không đổi header, footer, menu, CSS, light/dark, Quick Call, chatbot hoặc cơ chế 中文 / EN trong giai đoạn lập matrix.
- Không tự thêm ảnh thật, lượt review, chứng chỉ, giá/ưu đãi hoặc bảo đảm hoàn cọc không có nguồn.
- Không tạo GitHub Actions SEO, cron hoặc publish post cho đến khi người dùng duyệt bước sau.

## F. SEO-01 — live baseline, kiểm tra thực tế ngày 2026-10-10

**Trạng thái:** `BASELINE_PASS_WITH_LIMITATIONS` — kiểm tra kỹ thuật cơ bản đạt trên URL đã thử. **Không đánh dấu SEO tối ưu nội dung của 26 trang đã hoàn tất.** Toàn bộ hàng mục B vẫn là `TODO` cho tối ưu nội dung và kiểm chứng chuyên sâu.

Cách kiểm tra: tải lại nguồn trực tiếp từ `https://zh.rentbikehanoi.com` bằng truy vấn live (`maxAge=0`) và so với cấu hình Jekyll trong `main`. Báo cáo HTTP và markup dưới đây chỉ áp dụng tại thời điểm đo, không chứng minh trang đã được Google/Baidu index.

| URL kiểm tra | HTTP | Robots render | Canonical | H1 | Schema JSON-LD |
|---|---:|---|---|---:|---|
| `/` | 200 | index,follow | `https://zh.rentbikehanoi.com/` | 1 | JSON hợp lệ: WebSite, LocalBusiness, WebPage |
| `/prices/` | 200 | index,follow | `https://zh.rentbikehanoi.com/prices/` | 1 | JSON hợp lệ: WebSite, LocalBusiness, WebPage, BreadcrumbList |
| `/faq/` | 200 | index,follow | `https://zh.rentbikehanoi.com/faq/` | 1 | JSON hợp lệ: WebSite, LocalBusiness, WebPage, BreadcrumbList, FAQPage; 12 câu |
| `/blog/` | 200 | noindex,follow | `https://zh.rentbikehanoi.com/blog/` | 1 | JSON hợp lệ |
| `/topics/50cc/requirements/` | 200 | noindex,follow | `https://zh.rentbikehanoi.com/topics/50cc/requirements/` | 1 | JSON hợp lệ |
| `/topics/rental/` | 200 | index,follow | `https://zh.rentbikehanoi.com/topics/rental/` | 1 | JSON hợp lệ |
| `/robots.txt` | 200 | `User-agent: *`, `Allow: /` | — | — | `Sitemap: https://zh.rentbikehanoi.com/sitemap.xml` |
| `/sitemap.xml` | 200 | — | — | — | XML sitemap có đúng 12 `<loc>` riêng biệt, tất cả thuộc domain chính thức |

**Thực đo bổ sung:**
- Trên 3 trang money/trust chính (home, prices, FAQ), HTML cho biết ngôn ngữ `zh-CN`, có một meta description, một title, một H1; nguồn HTML có một JSON-LD parse hợp lệ; OG URL và canonical trùng đích; không thấy `github.io` hay HTTP links lạc vào các liên kết đã trích xuất.
- FAQ `FAQPage` có 12 câu từ dữ liệu đang hiển thị. Không có nghĩa chắc chắn Google cung cấp FAQ rich results.
- Sitemap có 12 URL và không đưa `/blog/` hoặc danh mục con `noindex` vào danh sách. `robots.txt` không chặn crawl toàn website.
- **Chưa kiểm chứng:** Google Search Console/Bing index coverage, redirect http→https/non-canonical, tất cả 26 URL, liên kết gãy toàn site, JS tương tác thực tế, Lighthouse/Core Web Vitals và truy cập từ bot Trung Quốc. Đây là các hạng mục riêng, không được suy diễn PASS.

**Kết luận SEO-01:** không phát hiện lỗi chặn index, canonical sai hoặc JSON-LD không parse được trên các trang chính đã kiểm tra; không chỉnh nội dung, cấu hình index, sitemap hay workflow. Chuyển sang bước 02: tối ưu trang thương mại `/` và `/prices/` đầu tiên, sau đó mới lần lượt xử lý các trang danh mục cha. Mỗi đợt 1–2 URL, có QA và xác nhận deploy.

## G. SEO-02 — tối ưu trang chủ và bảng giá, QA live ngày 2026-10-11

**Trạng thái:** `QA_PASS` cho đúng hai URL `/` và `/prices/` — nghĩa là thay đổi nội dung/SEO được triển khai và kiểm tra HTML sau khi deploy. **Không** chứng minh thứ hạng, organic traffic, Core Web Vitals hoặc index thực tế trong Search Console.

**Thay đổi đã triển khai:**
1. Trang chủ `/`: đưa từ khóa `河内摩托车租赁` vào H1, giới thiệu rõ mô hình thuê, giá tham khảo theo dữ liệu chung `_data/vehicles.json`, tiền cọc, vị trí Long Biên, 3 bước chuẩn bị trước thuê; CTA bảng giá + liên hệ thay vì CTA tới blog rỗng. Đồng bộ `250` chủ đề bằng `_data/china-plan.json` (không còn chữ 200 bài).
2. Bảng giá `/prices/`: H1 rõ ý định tìm kiếm giá; trả lời trực tiếp mức tham khảo/ngày của Honda Wave, Vision, Air Blade và 50cc bằng dữ liệu chung; giải thích giá ngày/tuần/tháng, khoản đặt cọc, các mức chưa công bố; CTA liên hệ và Zalo.
3. Bổ sung từ điển EN cho nội dung mới, giữ website Chinese-first và URLs hiện tại. **Không sửa** tiền trong `_data/vehicles.json`, CSS, schema chung, trang khác, sitemap, FAQ, DNS, CNAME, workflow hay nhà máy 250 bài.

**QA đã xác minh:**
- Pull request `#2` được squash-merge thành `c43ca221ef8ebc32c3f1de6facb04137459b52c5`; GitHub Pages Jekyll build và deploy **SUCCESS** (`run 38071021205`).
- Đo trực tiếp sau deploy: cả hai URL HTTP 200; canonical self-reference đúng `https://zh.rentbikehanoi.com`, `index,follow`, HTML `zh-CN`, đúng 1 H1 và JSON-LD parse hợp lệ.
- `/`: H1 hiển thị `河内摩托车租赁，先看价格与押金。` và nội dung kế hoạch 250 chủ đề; các giá tham khảo Honda Wave 150,000 ₫, Vision 200,000 ₫, 50cc 200,000 ₫ khớp dữ liệu tham chiếu.
- `/prices/`: H1 `河内摩托车租赁价格表`, trả lời trực tiếp `河内租摩托车一天多少钱？`, bảng giá 6 dòng, nội dung về tiền cọc và gói chưa công bố; các liên kết đến FAQ, contact đều có trên HTML.
- QA tĩnh: 2 permalink không đổi, 1 H1 mỗi trang, dictionary tiếng Anh có các chuỗi mới, các liên kết nội bộ mới đều đúng đường dẫn đã biết.

**Giới hạn:** Chưa có kiểm tra click/tương tác thực tế trên iPhone, GSC/Bing index coverage, keyword volumes, tốc độ PSI/CWV hay chuyển đổi thực. Không nhận định các mục này đã PASS.

**Dừng tại SEO-02.** Giai đoạn sau, nếu được duyệt: SEO-03 về NAP, thương hiệu và FAQ của `/about/`, `/contact/`, `/faq/` và template schema chung; mỗi lượt nhỏ, có rollback.
