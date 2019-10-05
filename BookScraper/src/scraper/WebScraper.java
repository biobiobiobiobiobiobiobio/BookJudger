package scraper;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class WebScraper {

	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver","G:\\chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		
		String initUrl = "https://www.goodreads.com/book/popular_by_date/2019/10";
        String expectedTitle = "Most Popular Books Published In October 2019";
        String title = "";
        
        driver.get(initUrl);
        
        title = driver.getTitle();
        
        if (title.contentEquals(expectedTitle)){
            System.out.println("Test Passed!");
        } else {
            System.out.println("Test Failed");
        }
       
        //close Chrome
        driver.close();
	}

}
