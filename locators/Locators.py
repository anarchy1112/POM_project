from selenium.webdriver.common.by import By


class BasicInfo:
    url='https://www.edureka.co/'


class GlobalLoc:
    login_XPATH="//span[@class='login_click login-vd giTrackElementHeader ']"
    register_XPATH="//span[contains(@class,'signup_click signup-vd giTrackElementHeader')]"
    search_XPATH="//input[@aria-label='Enter Course, Category or keyword']"


class HomePageLoc:

    cloudComp_XPATH="//a[@class='nav-link ga_category_upfront'][normalize-space()='Cloud Computing']"
    devOps_XPATH='//a[contains(@class,"nav-link ga_category_upfront")][normalize-space()="DevOps"]'
    bi_and_Visualization_XPATH='//a[contains(@class,"nav-link ga_category_upfront")][normalize-space()="BI and Visualization"]'
    dataScience_XPATH='//a[contains(@class,"nav-link ga_category_upfront")][normalize-space()="Data Science"]'
    programmingFrameworks_XPATH='//a[contains(@class,"nav-link ga_category_upfront")][normalize-space()="Programming & Frameworks"]'
    executivePrograms_XPATH='//a[contains(@class,"nav-link ga_category_upfront")][normalize-space()="Executive Programs"]'
    bigData_XPATH='//a[contains(@class,"nav-link ga_category_upfront")][normalize-space()="Big Data"]'
    cyberSecurity_XPATH='//a[contains(@class,"nav-link ga_category_upfront")][normalize-space()="Cyber Security"]'
    projectManagement_XPATH='//a[contains(@class,"nav-link ga_category_upfront")][normalize-space()="Project Management and Methodologies"]'
    browseCategories_XPATH="//a[contains(@class,'dropdown-toggle hidden-xs hidden-sm ga_browse_top_cat')]//span[contains(text(),'Categories')]"
    loggedInOptions_XPATH="//span[@class='webinar-profile-name']"
    myprofile_XPATH="//a[normalize-space()='My Profile']"


class RegisterPageLoc:
    email_XPATH="//input[@id='sg_popup_email']"
    privacyCheckbox_XPATH="//input[@id='tc_agree']"
    signUpbtn_XPATH="//button[normalize-space()='Sign Up']"
    phoneField_XPATH="//input[@id='sg_popup_phone_no']"
    phoneDropdown_XPATH="//div[@class='inputfld captcha_parent_input error']//select[@aria-label='prefix']"
    password_XPATH="//input[@id='signup_password']"
    passwordPageText_XPATH='//h4[normalize-space()="Let\'s Get Started"]'
    startLearningBtn_XPATH="//button[normalize-space()='Start Learning']"

class ProfilePageLoc:
    userEmail_XPATH="//span[@class='user-email']"
    userPhone_XPATH="//span[@class='user-number']"
    userDetailEdit_XPATH="//div[@class='col-lg-8 col-md-8 col-sm-12 col-xs-12 prof-career-other-details']//div[1]//div[1]//a[1]//i[1]"