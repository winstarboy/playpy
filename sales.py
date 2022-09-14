from operator import countOf
from playwright.sync_api import sync_playwright,expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page2 = context.new_page()
    
    page.set_default_timeout(0)
    
    #signing in
    page.goto("https://www.linkedin.com/uas/login?session_redirect=%2Fsales&fromSignIn=true&trk=cold_join_sign_in")
    expect(page).to_have_url("https://www.linkedin.com/uas/login?session_redirect=%2Fsales&fromSignIn=true&trk=cold_join_sign_in")
    
    #email or phone fills
    page.locator('[aria-label="Email or Phone"]').fill("kewinsebrodriguez@gmail.com")
    
    #password fill
    page.locator('[aria-label="Password"]').fill("starboy__3062")
    
    #sign in
    page.locator('[aria-label="Sign in"]').click()
    expect(page).to_have_url("https://www.linkedin.com/sales/index")
    
    #text=RPA-COE
    page.goto("https://www.linkedin.com/sales/search/people?page=&savedSearchId=50538485&sessionId=22IBRAl8TLWN2bk4XVaYEA%3D%3D")
    page.locator("#search-results-container").click();
    
    #moves down to get all the dom elements rendered
    for index in range(0,200,1):
        page.locator("#search-results-container").press("ArrowDown")
        
    rows = page.locator("(//a[@data-anonymize='person-name'])")
    count = rows.count()
    print(count)
    
    arr = []
    i = 0
    

    while i < count:
        
        obj = {}
        try:
            print(i)
            name = rows.nth(i).text_content();
            print(name)
            #name ? (obj.name = name?.replace(/[\r\n]+/gm, "").strip()) : "";
            link = page.locator("(//a[@data-anonymize='company-name'])").nth(i).text_content()
            cmp = page.locator("(//a[@data-anonymize='company-name'])").nth(i).get_attribute("href")
            print(link)
            print(cmp)
            if (cmp):
             url = "https://www.linkedin.com/"+ cmp;
            
            # obj.url = url
            if (url):
                page2.goto(url);
                page2.wait_for_load_state();
                x = page2.locator('a:has-text("Visit website Website")');

                x.wait_for()            
                if (x.count() == 1):
                    url =  x.get_attribute("href");
                    # obj.website = url;
                    # obj.website = null;
                    print(url)
                else:
                    print("null")
        except Exception as e:  
            print(e)
        i += 1
        
        
