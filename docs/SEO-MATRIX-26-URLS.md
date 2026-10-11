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
| SEO-03 | `/topics/rental/` | Danh mục cha | index,follow theo template | Trong sitemap | 河内摩托车租赁服务 | P0 | Làm rõ xe tay ga, số sàn, thuê dài hạn, chính sách giao nhận chỉ khi xác nhận. | QA_PASS |
| SEO-04 | `/topics/pricing/` | Danh mục cha | index,follow theo template | Trong sitemap | 河内摩托车租金指南 | P1 | Tập trung cách so sánh giá/đặt cọc; phân biệt rõ với /prices/ là bảng giá giao dịch. | QA_PASS |
| SEO-05 | `/topics/50cc/` | Danh mục cha | index,follow theo template | Trong sitemap | 河内50cc摩托车租赁 | P0 | Trình bày mẫu xe, chi phí, yêu cầu pháp lý kiểm chứng; không khẳng định miễn bằng lái. | QA_PASS |
| SEO-06 | `/topics/old-quarter/` | Danh mục cha | index,follow theo template | Trong sitemap | 河内老城区附近租摩托车 | P0 | Giải thích cửa hàng ở Long Biên, không nằm trong Phố Cổ; thêm dẫn đường thực tế, điều kiện giao xe. | QA_PASS |
| SEO-07 | `/topics/guides/` | Danh mục cha | index,follow theo template | Trong sitemap | 河内摩托车租赁指南 | P1 | Cấu trúc hướng dẫn/kiểm tra xe/an toàn và câu hỏi trước thuê, hạn chế trùng nội dung trang con. | QA_PASS |
| SEO-08 | `/about/` | Giới thiệu | index,follow theo template | Trong sitemap | Nguyễn Tú 河内摩托车租赁店 | P1 | Entity/NAP, thông tin cửa hàng có thể kiểm chứng, liên kết Maps và bằng chứng thực tế khi có. | QA_PASS |
| SEO-09 | `/contact/` | Liên hệ | index,follow theo template | Trong sitemap | Nguyễn Tú 河内租车联系方式 | P1 | Nổi bật địa chỉ, Zalo, điện thoại, giờ mở cửa, bản đồ; rà accessibility và mobile. | QA_PASS |
| SEO-10 | `/faq/` | FAQ | index,follow theo template | Trong sitemap | 河内租摩托车常见问题 | P1 | Kiểm tra 12 câu FAQ và giá/đặt cọc/luật, đồng bộ JSON-LD; FAQ rich result không được bảo đảm. | QA_PASS |
| SEO-11 | `/privacy/` | Pháp lý | index,follow theo template | Trong sitemap | Nguyễn Tú 隐私政策 | P3 | Rà soát độ đúng của mô tả dữ liệu lưu trữ, dịch vụ ngoài, liên hệ yêu cầu; duyệt chính sách. | TODO |
| SEO-12 | `/terms/` | Pháp lý | index,follow theo template | Trong sitemap | Nguyễn Tú 使用条款 | P3 | Rà soát điều kiện đặt xe, trách nhiệm/đặt cọc và tuyên bố giới hạn; duyệt pháp lý. | TODO |
| SEO-13 | `/blog/` | Hub bài viết | noindex khi 0 bài | Ngoài sitemap (0 bài) | 河内摩托车租赁中文博客 | P2 | Duy trì noindex khi 0 bài; mở index/sitemap chỉ khi có bài thật và nội dung hub hữu ích. | QA_PASS |
| SEO-14 | `/topics/rental/scooters/` | Danh mục con | noindex: true | Ngoài sitemap | 河内踏板车租赁 | P2 | Bổ sung mẫu xe, kiểm tra xe, giá dẫn về /prices/; duyệt chất lượng trước khi mở index. | QA_PASS |
| SEO-15 | `/topics/rental/monthly/` | Danh mục con | noindex: true | Ngoài sitemap | 河内摩托车月租 | P2 | Chi tiết khoảng giá/thời hạn/hợp đồng/chi phí đặt cọc, tránh trùng danh mục cha. | QA_PASS |
| SEO-16 | `/topics/rental/automatic/` | Danh mục con | noindex: true | Ngoài sitemap | 河内自动挡与手动挡摩托车 | P2 | So sánh đúng các kiểu xe, phù hợp người lái, nguồn an toàn, liên kết danh mục thuê. | QA_PASS |
| SEO-17 | `/topics/pricing/daily/` | Danh mục con | noindex: true | Ngoài sitemap | 河内摩托车日租价格 | P2 | Làm rõ mức thuê/ngày theo xe đã công bố, điều kiện tính ngày và khoản chưa bao gồm. | QA_PASS |
| SEO-18 | `/topics/pricing/weekly/` | Danh mục con | noindex: true | Ngoài sitemap | 河内摩托车周租价格 | P2 | Giá tuần cho xe có công bố; không tự suy ra gói 50cc/xe điện; liên kết bảng giá. | QA_PASS |
| SEO-19 | `/topics/pricing/deposits/` | Danh mục con | noindex: true | Ngoài sitemap | 河内租摩托车押金 | P2 | Bảng đặt cọc tham khảo theo mẫu, quy trình trả cọc đúng hợp đồng, nguồn công khai. | QA_PASS |
| SEO-20 | `/topics/50cc/models/` | Danh mục con | noindex: true | Ngoài sitemap | 河内50cc踏板车车型与价格 | P2 | Giá/ngày, mức cọc và mẫu 50cc thực tế, tình trạng xe cần xác minh. | QA_PASS |
| SEO-21 | `/topics/50cc/requirements/` | Danh mục con | noindex: true | Ngoài sitemap | 越南50cc摩托车驾驶规定 | P2 | Tài liệu quy định VN hiện hành, nguồn có ngày, tuổi/giấy phép/định nghĩa xe. | QA_PASS |
| SEO-22 | `/topics/old-quarter/directions/` | Danh mục con | noindex: true | Ngoài sitemap | 河内老城区到Long Biên租车店路线 | P2 | Google Maps và địa chỉ đúng; không bịa thời gian di chuyển hoặc lộ trình cố định. | QA_PASS |
| SEO-23 | `/topics/old-quarter/pickup/` | Danh mục con | noindex: true | Ngoài sitemap | 河内老城区取还摩托车咨询 | P2 | Phân biệt nhận xe tại cửa hàng và giao xe khi được xác nhận; chi phí/địa điểm phải hỏi. | QA_PASS |
| SEO-24 | `/topics/guides/contracts/` | Danh mục con | noindex: true | Ngoài sitemap | 河内租摩托车证件与合同 | P2 | Checklist giấy tờ/hợp đồng và đặt cọc; không yêu cầu hộ chiếu nếu không có chính sách chính thức. | QA_PASS |
| SEO-25 | `/topics/guides/safety/` | Danh mục con | noindex: true | Ngoài sitemap | 河内摩托车骑行安全 | P2 | Nguồn an toàn/pháp lý rõ; hướng dẫn kiểm tra xe và hạn chế hứa hẹn. | QA_PASS |
| SEO-26 | `/topics/guides/returns/` | Danh mục con | noindex: true | Ngoài sitemap | 河内摩托车还车与押金退还 | P2 | Đặt điều kiện trả xe và hoàn cọc theo hợp đồng; quy trình có xác minh. | QA_PASS |

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

## H. SEO-03 — About, Contact, FAQ & LocalBusiness Entity (2026-10-11)

**Trạng thái: QA_PASS** cho đúng ba URL `/about/`, `/contact/`, `/faq/`. Cập nhật một template schema dùng chung, nên đã kiểm tra thêm `/` nhằm tránh hồi quy toàn site. Không khẳng định đã có Google/Baidu index, rich result, cải thiện thứ hạng hoặc tăng traffic.

**Đã làm:**
- `/about/` — H1 rõ về Nguyễn Tú và thuê xe tại Hà Nội; hiển thị thương hiệu, tên Google Business Profile qua cấu hình NAP tập trung, địa chỉ và giờ Hà Nội, cách tự xác minh qua Google Maps và liên hệ; không hứa giao xe Phố Cổ.
- `/contact/` — title/description sát ý định tìm kiếm địa chỉ/điện thoại/Zalo; `ContactPage` trong front matter; hướng dẫn 3 bước trước khi thuê, nút gọi/Zalo, lưu ý không tự đặt hoặc trả tiền trực tuyến.
- `/faq/` — H1/sapo rõ nội dung giá/đặt cọc/50cc/nhận trả; giữ nguyên 12 FAQ thật từ `_data/faqs.json`; liên kết hỗ trợ đến `/prices/` và quy định 50cc.
- `_includes/schema.html` — nối `WebSite.publisher` → `LocalBusiness`, bổ sung `hasMap`/trang website chính, `AboutPage` và `ContactPage.mainEntity` trỏ đến doanh nghiệp; **một `FAQPage` có `@id` bằng trang FAQ và 12 Question/Answer từ nguồn chung** thay vì WebPage và FAQPage tách rời.
- `_data/i18n-en.json` — thêm các nhãn/đoạn EN có biên tập cho nội dung mới; HTML mặc định vẫn tiếng Trung.

**Bằng chứng kiểm tra:** PR [#3](https://github.com/thuexemayhanoi/china/pull/3) merge commit `737a98b65e76bf09c6dcd6a288ae5ab8f02d09dd`. GitHub Pages run `38071707146`: **Jekyll build SUCCESS / Deploy SUCCESS**. Live fetch `maxAge=0` sau deploy:

| URL | HTTP | Canonical / Robots / H1 / JSON-LD | Entity type | Kết quả |
|---|---:|---|---|---|
| `/about/` | 200 | đúng URL / index,follow / 1 H1 / JSON hợp lệ | AboutPage → LocalBusiness | QA_PASS |
| `/contact/` | 200 | đúng URL / index,follow / 1 H1 / JSON hợp lệ | ContactPage → LocalBusiness | QA_PASS |
| `/faq/` | 200 | đúng URL / index,follow / 1 H1 / JSON hợp lệ | FAQPage, 12 Q&A hiển thị và schema | QA_PASS |
| `/` (hồi quy schema) | 200 | đúng URL / index,follow / 1 H1 / JSON hợp lệ | WebPage + LocalBusiness | QA_PASS |

**Ràng buộc:** Không sửa CNAME/DNS, 26 permalink, robots/sitemap, CSS/menu/footer, bảng giá, widget, `/french` hay workflow/matrix 250 bài. QA này không thay thế Google Rich Results Test, Google Search Console, đo mobile thực tế hoặc kiểm toán pháp lý. **Tạm dừng tại SEO-03.**

## I. SEO-04 — Pricing hub & Rental Guides hub (2026-10-11)

**Trạng thái QA_PASS** chỉ cho hai danh mục cha: `/topics/pricing/` (`SEO-04`) và `/topics/guides/` (`SEO-07`). Không coi đây là xác nhận thứ hạng, Google/Baidu index, tốc độ hoặc chuyển đổi.

**Phân định search intent chống trùng nội dung:**
- `/prices/`: bảng giá công khai từng dòng xe, giá ngày/tuần/tháng và tiền cọc (trang giao dịch, đã QA ở SEO-02).
- `/topics/pricing/`: giải thích cách đọc báo giá, phân biệt tiền thuê/đặt cọc, lựa chọn chu kỳ thuê và các thông tin cần chuẩn bị khi xin báo giá. Không nhúng lại bảng giá; liên kết dẫn về `/prices/`, FAQ, Contact và 3 danh mục con.
- `/topics/guides/`: checklist bốn bước (trước thuê/giấy tờ, nhận xe/kiểm tra, đi đường/an toàn, trả xe/tiền cọc) thay vì lặp thông tin giá; liên kết đến hướng dẫn 50cc, an toàn, trả xe, FAQ và danh mục con.
- Cả hai giữ nguyên Jekyll `site.posts` dynamic topic listings, `sidebar`, hệ thống 中文/EN và giao diện; bổ sung bản dịch EN từ `_data/i18n-en.json`.

**GitHub:** PR [#4](https://github.com/thuexemayhanoi/china/pull/4) squash-merge commit `4635e8bce02fcc020ef74e6bdf5ebbaa92fcbc3a`. Jekyll build và GitHub Pages deploy run `38072158472` đều **SUCCESS**.

**QA source trước merge:** giới hạn thay đổi đúng 3 file (`topics/pricing/index.html`, `topics/guides/index.html`, `_data/i18n-en.json`). Mỗi trang một H1, 4 hoặc 5 H2, khoảng 721/748 chữ Hán trong source đã bỏ tags, meta description đủ nghĩa, internal links trỏ đúng URL, các đoạn mới có bản dịch EN; dữ liệu 6 mẫu xe và matrix 250 bài không đổi.

**Kiểm tra website trực tiếp sau deploy (`maxAge=0`):**

| URL | HTTP | Canonical | Robots/Language | H1 | H2 | JSON-LD | Kết quả |
|---|---:|---|---|---|---:|---|---|
| `/topics/pricing/` | 200 | self | index,follow / zh-CN | `河内摩托车租金与押金指南` | 4 | parse hợp lệ: WebSite, LocalBusiness, WebPage, BreadcrumbList | QA_PASS |
| `/topics/guides/` | 200 | self | index,follow / zh-CN | `河内摩托车租赁实用指南` | 5 | parse hợp lệ: WebSite, LocalBusiness, WebPage, BreadcrumbList | QA_PASS |

**Không thay đổi:** CNAME, DNS, canonical URL, robots, sitemap, template/schema chung, CSS, JS, header/footer, chatbot, Quick Call, 6 danh mục con vẫn `noindex` và 250 bài trong factory. **Chưa thực hiện** Google Search Console, PSI/Core Web Vitals, QA chạm thực tế iPhone hoặc xác minh luật 50cc theo nguồn văn bản pháp lý chuyên sâu. Dừng tại SEO-04 theo phạm vi duyệt.

## J. Lượt thủ công SEO-05 — Rental & 50cc hub (2026-10-11)

**Trạng thái:** `SEO-03` (`/topics/rental/`) và `SEO-05` (`/topics/50cc/`) → `QA_PASS` sau kiểm tra HTML trực tiếp. Đây là nghiệm thu thay đổi on-page/kỹ thuật của đúng hai trang, không chứng minh Google/Baidu đã index, thứ hạng tăng, Core Web Vitals hoặc rich results.

- Trang `/topics/rental/`: định vị từ khóa tiếng Trung về dịch vụ thuê xe Hà Nội, chọn Honda Wave/xe tay ga/50cc và xe điện dựa trên kinh nghiệm, các loại thời hạn, xác minh địa chỉ Long Biên và điều kiện giao/nhận, checklist trước hợp đồng; không cam kết tồn kho hoặc giao xe miễn phí.
- Trang `/topics/50cc/`: trả lời giá ngày 200,000 ₫ và cọc 4 triệu ₫ từ `_data/vehicles.json`; tuần/tháng báo giá riêng, kiểm tra thông số/xe, tuổi/điều kiện giấy phép theo luật hiện hành (không khẳng định miễn bằng lái); liên kết đến giá, FAQ thông qua những trang phù hợp và liên hệ.
- Cập nhật `_data/i18n-en.json` bổ sung 49 mục ngôn ngữ EN cho nội dung mới; không sửa CSS/JS, schema template, tên miền, sitemap, CNAME, giá/đặt cọc hay matrix bài viết 250 chủ đề. Giữ `site.posts` dynamic và sidebar.
- PR [#6](https://github.com/thuexemayhanoi/china/pull/6) squash-merge `385e684cf31195a7928f210eedd7c16b0300726d`. GitHub Pages Jekyll build/deploy **SUCCESS**: [run 38108353715](https://github.com/thuexemayhanoi/china/actions/runs/38108353715).
- QA tĩnh: đúng 3 file, mỗi trang 1 H1, 5/4 H2, link đến URL hợp lệ, từ điển EN đầy đủ cho text mới, nội dung tiếng Trung khoảng 912/721 Hán tự ở source (có phần UI chung), giá/cọc 50cc lấy dữ liệu tập trung.
- Kiểm tra live `maxAge=0` **sau deploy**:

| URL | HTTP | Canonical | Robots/lang | H1 | JSON-LD | Kết quả |
|---|---:|---|---|---|---|---|
| `/topics/rental/` | 200 | Self canonical đúng | index,follow / zh-CN | 1, đúng chủ đề | LocalBusiness + BreadcrumbList parse hợp lệ | QA_PASS |
| `/topics/50cc/` | 200 | Self canonical đúng | index,follow / zh-CN | 1, đúng chủ đề | LocalBusiness + BreadcrumbList parse hợp lệ | QA_PASS |

**Không nghiệm thu:** tương tác iPhone thực tế, GSC/Bing index, đo traffic/conversion, xác thực pháp lý riêng từng trường hợp hoặc Core Web Vitals. Không đổi robots/noindex của 13 trang con. **Dừng lượt thủ công tại 9/26**, chờ duyệt bước kế tiếp.

## K. SEO-06 — Old Quarter danh mục cha (2026-10-11)

**Kết quả:** `SEO-06` cho đúng URL `/topics/old-quarter/` → **QA_PASS** sau khi đã kiểm tra Jekyll build/deploy và HTML trang thật. Đây không phải xác nhận Google/Baidu index, ranking, Core Web Vitals hay chuyển đổi.

- Đã phân định đúng ý định tìm kiếm “thuê xe máy từ Phố Cổ Hà Nội”: cửa hàng Nguyễn Tú **ở 112 Nguyễn Văn Cừ, Bồ Đề, Long Biên**, không nằm trong Phố Cổ; tránh mô tả là cơ sở ngay tại Phố Cổ.
- H1/title/description tiếng Trung nhấn mạnh vị trí và hướng dẫn khách từ Phố Cổ. Bổ sung cách dùng Google Maps, tránh tự bịa km/phút; giờ và địa chỉ lấy từ nguồn NAP chung.
- Nêu rõ nhận xe tại cửa hàng khác với giao xe hoặc nhận trả ở địa điểm khác; phải liên hệ xác nhận địa điểm, lịch và phí phát sinh. Không mặc định giao miễn phí, có tồn kho, hay đặt trước tự động.
- Bổ sung checklist trước chuyến đi và internal links đến `/prices/`, `/contact/`, `/faq/`, `/topics/guides/`, hai trang con cùng Google Maps. Bổ sung 29 mục dịch EN; giữ giao diện 中文-first.
- Chỉ chỉnh **2 file** `topics/old-quarter/index.html` và `_data/i18n-en.json`. Không đụng `/topics/old-quarter/directions/` (`SEO-22`) hoặc `/topics/old-quarter/pickup/` (`SEO-23`); hai trang con vẫn `noindex`, **chưa QA_PASS**. Không sửa CNAME, DNS, robots, sitemap, giá, schema chung, CSS/JS/menu, chatbot, factory 250 bài.
- PR [#7](https://github.com/thuexemayhanoi/china/pull/7) squash-merge `91422e8c966b0c82fe34dea7af6ca0a01dd7048c`. [GitHub Pages run 38108696436](https://github.com/thuexemayhanoi/china/actions/runs/38108696436) **Jekyll build/deploy SUCCESS**.
- QA trang thật `https://zh.rentbikehanoi.com/topics/old-quarter/` (`maxAge=0`): **HTTP 200**, self-canonical đúng, `index,follow`, `zh-CN`, đúng 1 H1 `从河内老城区出发租摩托车：门店与取还车指南`, 5 H2, LocalBusiness/BreadcrumbList JSON-LD hợp lệ; có địa chỉ, giờ 09:00–21:00, Google Maps, và liên kết liên hệ. Câu phủ định lời hứa giao miễn phí, đại diện Phố Cổ hiển thị đúng.

**Sau lượt này:** 10/26 URL `QA_PASS`, 16 URL chưa hoàn thành. Giữ lịch tự động OFF; chỉ tiếp tục khi người dùng duyệt thủ công.

## L. Lượt SEO thủ công — Rental Scooters & Monthly child guides (2026-10-11)

**Trạng thái:** `SEO-14` `/topics/rental/scooters/` và `SEO-15` `/topics/rental/monthly/` → `QA_PASS` **chỉ về phần tối ưu nội dung/kỹ thuật đã QA sau deploy**. Cả hai **cố ý giữ `noindex,follow`**, ngoài sitemap, và không được coi là Google/Baidu đã index, ranking tốt hơn hay đủ điều kiện bắt buộc phải mở index. Quyết định mở index cần đánh giá riêng về tính độc lập, nội dung, GSC/intent và mức trùng lặp với trang cha, chưa được thực hiện.

**Thay đổi nhỏ đã xác nhận:**
- `/topics/rental/scooters/`: H1, title và description mô tả hướng dẫn thuê scooter; 4 phần gồm Honda Vision/Air Blade/Click-Mio với giá/ngày và tiền cọc tham khảo lấy trực tiếp `_data/vehicles.json`, cách chọn xe, checklist giao xe, địa chỉ/cách liên hệ; hướng link về bảng giá, rental hub và guides. Không cam kết số lượng xe/giá chốt hoặc miễn phí giao xe.
- `/topics/rental/monthly/`: 4 phần riêng về mức giá/tháng, tiền cọc của 4 nhóm xe xuất phát từ dữ liệu chung, cách xác định kỳ tháng, gia hạn/trả sớm, trách nhiệm bảo trì/bàn giao, checklist xin báo giá; không tự suy ra giá 50cc/xe điện, không coi tất cả giá tháng là giá chắc chắn.
- `_data/i18n-en.json`: thêm 50 khóa dịch EN cho nội dung mới, giữ site Chinese-first và công tắc dịch hiện có. Diff được giới hạn 3 file; không sửa dữ liệu giá, URL, NAP, robots, sitemap, CSS/JS, schema template, menu/footer, DNS/CNAME hoặc factory 250 bài.

**GitHub:** [PR #8](https://github.com/thuexemayhanoi/china/pull/8) merge commit `60d84b5c67b2aed95f2b521e3c545aa7e097dd4d`, [GitHub Pages run 38109256857](https://github.com/thuexemayhanoi/china/actions/runs/38109256857) **Build with Jekyll và Deploy SUCCESS**.

**QA HTML thực tế sau deploy (maxAge=0):**

| URL | HTTP | Canonical | Robots | HTML | Giá/CTA/schema | Kết quả |
|---|---:|---|---|---|---|---|
| `/topics/rental/scooters/` | 200 | self đúng | `noindex,follow` (giữ nguyên) | `zh-CN`, 1 H1, 4 H2, title/description mới | Vision 200k/ngày cọc 4–5m; Air Blade 200k cọc 3m; Click/Mio 150k cọc 2m; links và LocalBusiness/BreadcrumbList parse hợp lệ | QA_PASS nội dung |
| `/topics/rental/monthly/` | 200 | self đúng | `noindex,follow` (giữ nguyên) | `zh-CN`, 1 H1, 4 H2, title/description mới | 4 mức tháng từ dữ liệu gốc, không suy ra 50cc/electric, links và schema hợp lệ | QA_PASS nội dung |

**Giới hạn:** Không đo Core Web Vitals, index coverage/GSC, giao diện iPhone tương tác thực tế, tìm kiếm SERP hay tác động chuyển đổi. Bản QA này là nghiệm thu biên tập/tính đúng của HTML và chiến lược giữ noindex, không phải giấy phép mở index. Tiến độ **12/26 QA_PASS**, 14 hạng mục còn lại.

## M. Lượt thủ công SEO-16/17 — Automatic & Daily pricing child guides (2026-10-11)

**Trạng thái:** `SEO-16` `/topics/rental/automatic/` và `SEO-17` `/topics/pricing/daily/` → **QA_PASS chỉ cho nội dung & QA HTML sau deploy**. Hai URL vẫn `noindex,follow`, không nằm sitemap. Chưa quyết định mở index. Không khẳng định Google/Baidu index, SERP/traffic, chuyển đổi hoặc CWV cải thiện.

**Phạm vi thay đổi:**
- `/topics/rental/automatic/` — phân biệt xe tay ga số tự động, xe bán tự động (một số đời Honda Wave cần đạp số nhưng không có tay côn truyền thống) và xe côn tay, **không khẳng định cửa hàng có sẵn xe côn tay**. Hướng dẫn chọn theo kinh nghiệm, kiểm tra phanh/lốp/đèn/mũ bảo hiểm và đối chiếu điều kiện lái xe theo luật đang áp dụng. Dẫn nguồn thông tin chính thức `https://www.csgt.vn/`, không chép lại quy định pháp lý chưa kiểm chứng; link về danh mục thuê, scooter, bảng giá, an toàn và contact.
- `/topics/pricing/daily/` — H1, title/meta về giá thuê ngày; 5 dòng xe có giá/ngày và đặt cọc lấy trực tiếp `_data/vehicles.json`, không hardcode mức trong phần body; riêng xe điện không công bố, tuần/tháng 50cc phải hỏi. Không khẳng định ngày thuê tính tròn 24h: nêu rõ phải xác nhận giờ bắt đầu/kết thúc, phát sinh và loại phí. Link về giá, danh mục giá, giá tuần, cọc và liên hệ.
- `_data/i18n-en.json` bổ sung 53 mục dịch EN; ba file duy nhất. Không đổi dữ liệu gốc về giá/cọc, template chung, schema, CSS, menu, sitemap, robots, CNAME, DNS, chatbot hoặc factory 250 bài.

**Bằng chứng GitHub:** [PR #9](https://github.com/thuexemayhanoi/china/pull/9) squash-merge `e6520c756c5fd5aa486afebe02d68b3d1a0686cf`. [Pages run 38109629533](https://github.com/thuexemayhanoi/china/actions/runs/38109629533) **Jekyll build và deploy SUCCESS**.

**QA HTML live** (request `maxAge=0`, sau deploy):
| URL | HTTP | Canonical | Robots | H1/H2 | Schema & nội dung | Kết luận |
|---|---:|---|---|---|---|---|
| `/topics/rental/automatic/` | 200 | self đúng | `noindex,follow` | 1 H1, 4 H2, `zh-CN` | LocalBusiness + BreadcrumbList JSON-LD parse hợp lệ; link cơ quan CSGT, không hứa miễn phép lái hay có xe côn tay | QA_PASS nội dung |
| `/topics/pricing/daily/` | 200 | self đúng | `noindex,follow` | 1 H1, 4 H2, `zh-CN` | 150k/200k VND theo 5 mẫu, cọc từng mẫu, điều kiện tính ngày và link nội bộ; JSON-LD hợp lệ | QA_PASS nội dung |

**Giới hạn nghiệm thu:** Chưa kiểm tra GSC index coverage, mobile tương tác thật, Core Web Vitals, keyword rankings hoặc thay đổi chuyển đổi. `QA_PASS` không đồng nghĩa trang con đã/được mở index. **Tiến độ 14/26; chờ duyệt thủ công bước tiếp theo.**

## N. Lượt thủ công SEO-18/19 — Giá thuê tuần và tiền cọc (2026-10-11)

**Trạng thái:** `SEO-18` (`/topics/pricing/weekly/`) và `SEO-19` (`/topics/pricing/deposits/`) chuyển **QA_PASS đối với nội dung và HTML đã kiểm tra sau deploy**. Cả hai URL giữ `noindex,follow`, nằm ngoài sitemap và không được tuyên bố là đã index hoặc xếp hạng. Việc mở index, đánh giá tính độc lập với pricing hub vẫn là quyết định riêng.

- **Weekly:** Bốn nhóm xe có giá tuần công khai lấy trực tiếp từ `site.data.vehicles[0..3].display.week` và tiền cọc từ `deposit`: Wave 700k ₫; Vision và Air Blade 1m ₫; Click/Mio 700k ₫. 50cc và xe điện không có tuần công khai nên chỉ đề nghị hỏi trực tiếp; không suy ra bằng phép nhân từ giá ngày. Nội dung bổ sung định nghĩa kỳ thuê cần xác nhận, gia hạn, phí giao/nhận, so sánh ngày/tuần/tháng; internal links về price list, daily, monthly, deposits, contact.
- **Deposits:** Năm dòng cọc đã công bố từ `_data/vehicles.json` (Wave 2–3m ₫, Vision 4–5m ₫, Air Blade 3m ₫, Click/Mio 2m ₫, 50cc 4m ₫); cọc xe điện chưa niêm yết và phải xác nhận theo mẫu. Phân biệt tiền thuê/cọc; checklist hợp đồng, bằng chứng xe trước/sau, xác minh các khoản khấu trừ và điều kiện trả cọc, không tự bịa thời hạn hoàn cọc hoặc bảo đảm trả đủ. Liên kết về bảng giá, terms, return guide và contact.
- Cập nhật từ điển `_data/i18n-en.json` (+53 mục). PR chỉ chỉnh ba file: `topics/pricing/weekly/index.html`, `topics/pricing/deposits/index.html`, `_data/i18n-en.json`; không sửa bảng giá nguồn, NAP, schema/layout chung, JS/CSS, CNAME, DNS, sitemap/robots, widget, sidebar, menus hay workflow 250 bài.
- GitHub: [PR #10](https://github.com/thuexemayhanoi/china/pull/10) squash merge `4c5efa548ed8679405f10c28a3264a75e14d405a`. [Pages run 38110952664](https://github.com/thuexemayhanoi/china/actions/runs/38110952664) **build/deploy SUCCESS**.
- QA nguồn: mỗi trang 1 H1, 4 H2, nội dung tiếng Trung chuyên biệt, liên kết nội bộ đúng, bản dịch EN không thiếu text node, Liquid lấy giá/cọc từ nguồn chung, không gỡ `noindex: true`.

| Trang live (maxAge=0 sau deploy) | HTTP | Canonical | Robots | Kết quả HTML và dữ liệu |
|---|---:|---|---|---|
| `/topics/pricing/weekly/` | 200 | đúng self-canonical | `noindex,follow`, `zh-CN` | 1 H1, 4 H2, LocalBusiness/BreadcrumbList JSON-LD parse hợp lệ; giá tuần 700k/1m và các khoản cọc đúng; nội dung 50cc/electric không giá tuần |
| `/topics/pricing/deposits/` | 200 | đúng self-canonical | `noindex,follow`, `zh-CN` | 1 H1, 4 H2, LocalBusiness/BreadcrumbList JSON-LD parse hợp lệ; năm mức cọc từ nguồn chuẩn; không cam kết refund time; links hữu ích |

**Chưa đo:** Google Search Console indexing, ranking, CTR, traffic, tương tác thực tế trên iPhone, Core Web Vitals và tư vấn pháp lý về từng hợp đồng. Lượt SEO thủ công này kết thúc tại **16/26 QA_PASS, còn 10 URL**; lịch SEO tự động vẫn tắt.

## O. SEO-20/21 — 50cc Models & Requirements (lượt duyệt thủ công 2026-10-11)

**Trạng thái:** `SEO-20` `/topics/50cc/models/` và `SEO-21` `/topics/50cc/requirements/` → `QA_PASS` **về biên tập/source + QA HTML sau deploy**. Cả hai trang vẫn giữ `noindex,follow` và **không xuất hiện trong sitemap** theo chiến lược ban đầu; QA_PASS không có nghĩa Google/Baidu đã index hoặc tăng rank.

- **50cc Models:** Phân biệt danh mục 50cc chung với model thực tế/chất lượng/tồn kho chưa được xác minh; không tự gắn thương hiệu hay cam kết còn xe. Hiển thị giá tham khảo **200,000 ₫ mỗi ngày** và **cọc 4 triệu ₫** qua `site.data.vehicles[4]`, tuyệt đối không tự đặt giá thuê tuần/tháng (chưa công bố). Thêm checklist xác minh thông số xe, kiểm tra khi giao/nhận, hợp đồng và liên hệ, link tới `/prices/`, `/topics/50cc/requirements/`, `/contact/`.
- **50cc Requirements:** Trích dẫn Luật Trật tự, an toàn giao thông đường bộ **36/2024/QH15**, ngày **27/06/2024**, hiệu lực từ **01/01/2025**. Dẫn văn bản Chính phủ `https://xaydungchinhsach.chinhphu.vn/toan-van-luat-trat-tu-an-toan-giao-thong-duong-bo-119240909105718285.htm` và hồ sơ luật `https://vanban.chinhphu.vn/?classid=1&docid=211194&orggroupid=1&pageid=27160`. Điều **34**: loại `xe gắn máy` phụ thuộc tốc độ thiết kế không quá 50km/h, xe động cơ nhiệt không quá 50cm³, xe điện không quá 4kW, và điều kiện phân loại khác; Điều **56**: phân biệt yêu cầu bằng lái với xe gắn máy đúng loại và vẫn yêu cầu kỹ năng, hiểu biết luật, tuổi, sức khỏe; Điều **59**: người từ đủ 16 tuổi có thể điều khiển xe gắn máy đúng định nghĩa. Nội dung có lưu ý riêng cho người nước ngoài/chứng nhận lái và phải kiểm tra sửa đổi pháp luật sau ngày **11/10/2026**, không tuyên bố mọi xe quảng cáo 50cc đều được miễn giấy phép.
- **Source review:** thay đúng 3 file `topics/50cc/models/index.html`, `topics/50cc/requirements/index.html`, `_data/i18n-en.json` (+51 mục EN). Hai trang 1 H1/4 H2, dùng sidebar, `topic-posts` động. Không đổi bảng giá, NAP, CSS/JS, schema template, header/footer, CNAME/DNS, sitemap, factory 250 bài hoặc `noindex`. Giữ trang danh mục cha SEO-05 đã PASS.
- **GitHub:** [PR #11](https://github.com/thuexemayhanoi/china/pull/11) squash-merge `c288d04b29d6fa4ade9d18c23bf396144cb853be`; [GitHub Pages deploy 38111537170](https://github.com/thuexemayhanoi/china/actions/runs/38111537170) **SUCCESS**.
- **Live HTML QA (maxAge=0):** cả `/topics/50cc/models/` và `/topics/50cc/requirements/` HTTP 200, đúng self canonical, `noindex,follow`, `zh-CN`, đúng 1 H1, 4 H2 mới, JSON-LD có LocalBusiness và BreadcrumbList hợp lệ, liên kết qua contact và danh mục cha đúng. Models hiển thị 200k/4m giá-cọc và không hứa brand/stock; Requirements hiển thị đầy đủ Điều 34/56/59, nguồn luật cùng ngày hiệu lực.
- **Chưa QA:** GSC indexing, legal interpretation cho từng người/xe, thực tế ảnh đội xe/thông số xe cụ thể, iPhone tương tác, Core Web Vitals, chuyển đổi hoặc SEO ranking.

**Sau lượt này: 18/26 `QA_PASS`, còn 8 hạng mục.** Các trang con vẫn noindex trừ khi được duyệt mở index riêng; lịch chạy tự động vẫn OFF.

## P. SEO-22/23 — Directions & Pickup Old Quarter (duyệt thủ công 2026-10-11)

**Đánh dấu:** `SEO-22` `/topics/old-quarter/directions/` và `SEO-23` `/topics/old-quarter/pickup/` thành **QA_PASS chỉ về nội dung + cấu trúc HTML đã kiểm chứng sau deploy**. Hai trang con vẫn **`noindex,follow`** và **ngoài sitemap**, không có tuyên bố Google/Baidu đã index hay lưu lượng, ranking, Core Web Vitals cải thiện.

- `/topics/old-quarter/directions/`: H1/meta tập trung truy vấn hướng dẫn từ Phố Cổ đến cửa hàng Long Biên. Nêu **địa chỉ 112 Nguyễn Văn Cừ, Bồ Đề, Long Biên** và giờ 09:00–21:00 từ `_data/site.json`, link trực tiếp Google Maps CID và hướng dẫn nhập **điểm xuất phát thật** để kiểm tra tuyến, giao thông và thời gian từ bản đồ. Không bịa km, thời gian di chuyển, cây cầu/lộ trình bắt buộc. Thêm danh sách xác minh tồn kho, báo giá, giao xe và kiểm tra tình trạng xe trước ký hợp đồng.
- `/topics/old-quarter/pickup/`: Giải thích nhận/trả tại **cửa hàng ở Long Biên** khác với trường hợp xin giao/nhận tại khách sạn, Phố Cổ hay địa điểm khác. Giao nhận ngoài cửa hàng không mặc định được cung cấp; phải **xác nhận rõ vị trí, thời gian, người giao nhận và mọi khoản phí** với cửa hàng. Không cam kết giao miễn phí, hàng sẵn có, đặt chỗ tự động, thời hạn hoặc hoàn đủ tiền cọc. Nêu checklist kiểm tra xe, chứng từ và đối chiếu hợp đồng khi trả.
- Mỗi trang 1 H1, 4 H2 nội dung riêng (trước sửa chỉ 1 H2); bản dịch EN bổ sung 60 mục trong `_data/i18n-en.json`. Diff chỉ **ba file**: `topics/old-quarter/directions/index.html`, `topics/old-quarter/pickup/index.html` và `_data/i18n-en.json`. Không sửa dữ liệu giá, địa chỉ nguồn, sidebar/layout/JSON-LD, CSS/JS, Quick Call/chatbot, sitemap/robots, CNAME/DNS hoặc workflow 250 bài.
- [PR #12](https://github.com/thuexemayhanoi/china/pull/12) squash merge `2825593223ce9f3d6bf66fe108ccddd513d65c7f`. [GitHub Pages run 38112068491](https://github.com/thuexemayhanoi/china/actions/runs/38112068491) **Jekyll build + deploy SUCCESS**.
- **Live QA** sau deploy `maxAge=0`:
  - `/topics/old-quarter/directions/`: HTTP 200, self canonical, `noindex,follow`, `zh-CN`, 1 H1/4 H2, valid LocalBusiness + BreadcrumbList JSON-LD; đúng NAP, Maps, links giá/contact, cảnh báo không đưa thời gian tuyến cố định.
  - `/topics/old-quarter/pickup/`: HTTP 200, self canonical, `noindex,follow`, `zh-CN`, 1 H1/4 H2, valid LocalBusiness + BreadcrumbList JSON-LD; đúng NAP, Maps/contact và lời giải thích không có cam kết giao miễn phí hoặc hoàn cọc tự động.

**Giới hạn QA:** Không đo thiết bị thật iPhone, GSC index/hiệu suất từ khóa, Core Web Vitals, chất lượng đường đi thực tế từng điểm xuất phát hoặc khả năng cung cấp giao nhận của cửa hàng. Giữ lịch SEO tự động OFF. **Tiến độ sau lượt này: 20/26 QA_PASS; còn 6 hạng mục**.

## Q. SEO-24/25 — Rental Contracts & Safety Guides (lượt duyệt thủ công 2026-10-11)

**Nghiệm thu:** `SEO-24` `/topics/guides/contracts/` và `SEO-25` `/topics/guides/safety/` → **QA_PASS về nội dung/kỹ thuật đã QA sau deploy**. Hai URL tiếp tục `noindex,follow` (ngoài sitemap); không có nghĩa đã được Google/Baidu index, thứ hạng hoặc lượt truy cập tăng.

- **Contracts:** Hướng dẫn xác nhận giấy tờ tùy theo người/xe, kiểm tra điều kiện lái xe riêng với điều kiện hợp đồng, bảo đảm không tự tuyên bố cửa hàng đòi nộp hay giữ hộ chiếu nguyên bản. Có bốn phần về giấy tờ, nội dung hợp đồng (thời gian/xe/trách nhiệm/chi phí), chứng từ/ảnh bàn giao và điều kiện hoàn cọc; nêu rõ không có chính sách mặc định hoàn đủ cọc hoặc hoàn sau số ngày cố định. Liên kết đến 50cc requirements, bảng giá, deposits, safety, returns và contact.
- **Safety:** Hướng dẫn kiểm tra lốp, phanh, đèn và mũ bảo hiểm; khu vực giao lộ Hà Nội, trời mưa, mệt mỏi và tránh lái xe không phù hợp kỹ năng; xử lý hỏng xe/tai nạn, kiểm tra giấy phép theo loại xe. Trích **Điều 33 Luật Trật tự, an toàn giao thông đường bộ 36/2024/QH15** (qua [Cổng thông tin Chính phủ](https://xaydungchinhsach.chinhphu.vn/toan-van-luat-trat-tu-an-toan-giao-thong-duong-bo-119240909105718285.htm), có hiệu lực 01/01/2025), bài [WHO 2023 về mũ bảo hiểm](https://www.who.int/news/item/05-04-2023-new-who-guide-aims-to-boost-the-use-of-life-saving-helmets-for-motorcycle-riders) và [NHTSA pre-ride](https://www.nhtsa.gov/road-safety/motorcycles). Không quảng cáo tiêu chuẩn DOT của Hoa Kỳ là quy chuẩn duy nhất tại VN, không hứa phòng được mọi tai nạn. Nội dung nguồn được rà ngày 11/10/2026; cần kiểm tra sửa đổi pháp luật khi sử dụng thực tế.
- **GitHub:** [PR #13](https://github.com/thuexemayhanoi/china/pull/13) squash-merge `feea5ec8d45849a6a52d024f081fa7a8cf25ad70`; [Pages run 38112521104](https://github.com/thuexemayhanoi/china/actions/runs/38112521104) **Jekyll build/deploy SUCCESS**. Thay đúng 3 file `topics/guides/contracts/index.html`, `topics/guides/safety/index.html` và `_data/i18n-en.json` (+58 mục dịch EN). Mỗi trang đúng 1 H1/4 H2; giữ `noindex: true`, layout/sidebar, dynamic `topic-posts`; không đổi nội dung NAP, giá, CSS/JS, schema template, CNAME/DNS, sitemap, Quick Call, chatbot, factory 250 bài hay repo khác.
- **Live QA** `maxAge=0` **sau deploy**: cả hai URL HTTP **200**, self-canonical đúng, `noindex,follow`, `zh-CN`, 1 H1/4 H2, LocalBusiness + BreadcrumbList JSON-LD hợp lệ, link nội bộ đến `/contact/` và `/topics/guides/` đúng; nội dung disclaimer hộ chiếu/hoàn cọc và nguồn WHO/luật hiển thị như thiết kế.

**Giới hạn:** Chưa xác minh chính sách giấy tờ thực tế từng giao dịch của cửa hàng, không có tư vấn pháp lý riêng người/xe, chưa đo thứ hạng GSC, mobile interaction iPhone, Core Web Vitals, chuyển đổi/traffic. Hai hạng mục được nghiệm thu **về nội dung trang khi vẫn noindex**, không phải duyệt mở index. **Tiến độ 22/26, còn 4 hạng mục**, lịch SEO tự động tiếp tục OFF chờ duyệt thủ công.

## R. SEO-26 & SEO-13 — Returns and empty Blog hub (duyệt thủ công 2026-10-11)

**Trạng thái:** `SEO-26` `/topics/guides/returns/` và `SEO-13` `/blog/` → **QA_PASS trong phạm vi nội dung và hành vi index khi blog chưa có bài**, sau khi Jekyll build, GitHub Pages deploy và QA URL thật. Không kết luận Google/Baidu đã index, ranking/traffic tăng, hoặc đã nghiệm thu trạng thái blog sau khi đăng bài mới.

- **SEO-26 (Returns):** Có hướng dẫn 4 phần: xác nhận thời gian/địa điểm trả xe, so sánh xe với ảnh giao nhận và ghi nhận tình trạng, tách tiền cọc khỏi tiền thuê/chi phí phát sinh, bảo quản chứng từ/trao đổi. Không tự dựng chính sách cố định về ngày hoàn cọc, hoàn đủ cọc hoặc miễn phí giao/trả xe. Links tới contracts, deposits, pricing, pickup/contact và guide hub; giữ `noindex: true`, ngoài sitemap.
- **SEO-13 (Blog):** GitHub tree trước/sau thay đổi đều **không có tệp dưới `_posts/`** (0 bài). Trang hiển thị trạng thái trung thực `0 篇`, không tạo bài/hyperlink giả. H1, meta title/description và nội dung giới thiệu được tinh chỉnh, 5 category cards cập nhật mô tả đúng các chủ đề thực có. `_includes/blog-posts.html` **vẫn liệt kê đúng `site.posts` tự động**; không sửa bản sinh bài 250 bài hoặc giả số lượng nội dung.
- **Robots & Sitemap:** `_layouts/default.html` hiện có quy tắc blog `noindex,follow` khi `site.posts.size == 0`; quy tắc này được **giữ nguyên**, không mở index khi rỗng. `sitemap.xml` có thêm điều kiện `{% if site.posts.size > 0 %}` trước khi xuất URL `/blog/`. Khi 0 bài, sitemap xuất đúng **12 URL cơ sở** và không chứa blog. Chỉ khi có post thật thì Jekyll mới dự kiến xuất blog hub và URL post. **Nhánh có bài thật chưa được chạy QA live** và vẫn phải xác nhận nội dung hub hữu ích/quality trước khi coi là index-ready cho Google.
- Đã bổ sung 41 mục EN translation vào `_data/i18n-en.json`. Chỉ 4 file thay đổi: `topics/guides/returns/index.html`, `blog/index.html`, `sitemap.xml`, `_data/i18n-en.json`. Không sửa dữ liệu giá/NAP, CNAME/DNS, template robot, JS/CSS, thiết kế, Quick Call, chatbot, các post hay repo khác.
- [PR #14](https://github.com/thuexemayhanoi/china/pull/14) squash merged `822eea3ebf9093a2caf1f98180a8c112424bfd45`; [GitHub Pages run 38113177712](https://github.com/thuexemayhanoi/china/actions/runs/38113177712) **Build & Deploy SUCCESS**.
- QA live `maxAge=0`, sau deploy: `/topics/guides/returns/` HTTP 200, self canonical, `zh-CN`, `noindex,follow`, 1 H1/4 H2, JSON-LD LocalBusiness + BreadcrumbList hợp lệ và các liên kết đúng; `/blog/` HTTP 200, self canonical, `zh-CN`, `noindex,follow`, 1 H1/2 H2 (gồm thông báo rỗng), hiển thị 0 bài và 5 topic hubs thật. `/sitemap.xml` HTTP 200, XML `urlset` hợp lệ về cấu trúc, 12 URL trong `sitemap_base`, **không có blog**, không có URL bài giả.

**Giới hạn QA:** Chưa kiểm tra trên thiết bị iPhone thực tế, GSC indexing, CWV, traffic/ranking, hợp đồng hoặc chính sách hoàn cọc của cửa hàng cho từng người, chưa test thực tế luồng blog sau khi thêm bài đầu tiên. Tiến độ nội dung/QA: **24/26 QA_PASS, còn SEO-11 Privacy và SEO-12 Terms**. Lịch SEO tự động vẫn OFF; tiếp tục theo phê duyệt thủ công.
