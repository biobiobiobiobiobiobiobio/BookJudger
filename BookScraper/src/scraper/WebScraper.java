package scraper;

import org.openqa.selenium.By;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebElement;


import java.awt.image.BufferedImage;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.net.URL;

import javax.imageio.ImageIO;

public class WebScraper {
	//Expected image dimensions
	//private static int width = 50, height = 75;
	
	//Number of list elements to read
	private static int numOfBooks = 200;
	
	//Index file name/location
	private static String indexFile = "../../books/index.txt";
	
	public static void main(String[] args) {
		//Setup the webdriver
		System.setProperty("webdriver.chrome.driver","C:\\WebDrivers\\chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		
		//Startup values
		String initUrl = "https://www.goodreads.com/book/popular_by_date/2018/January/";
        String expectedTitle = "Most Popular Books Published In January 2018";
        String title = "";
        
        //Check to see if the page even opened
        try {
	        driver.get(initUrl);
	        title = driver.getTitle();
        }catch(Exception e) {
        	e.printStackTrace();
        }
        
        if (title.contentEquals(expectedTitle)){
        	//Initial File name incremement
            int fileChrono = 1;
            try {
				BufferedWriter writer = new BufferedWriter(new FileWriter(indexFile));
				while(!title.equals("Most Popular Books Published In November 2019")) {
						
		            //Over all 200 list entries
		            for(int i = 1; i <= numOfBooks; i ++) {
		            	//Find the next sequential image
			            WebElement image = driver.findElement(By.cssSelector("tr:nth-child(" + i + ") .bookCover"));
			            String src = image.getAttribute("src");
			            
		//Get the image
		//BufferedImage bufferedImage;
			            try {	
			            	//Actually get the image
			            	BufferedImage bufferedImage = ImageIO.read(new URL(src));
			            	File outputfile = new File("../../books/" + fileChrono + ".jpg");
				            ImageIO.write(bufferedImage, "jpg", outputfile);
				            	
					        //Get the rating
					        WebElement review = driver.findElement(By.cssSelector("tr:nth-child(" + i + ") .minirating"));
					        String rating = getRating(review);
					           
					        //writer.write(i + " ");
					        writer.write(rating + "\n");
					            
					        //Stored a book, increment for the next
					        fileChrono ++;
			            }catch(IOException e) {
			            	//You fucked up...
			            	e.printStackTrace();
			            }
		            }
		            WebElement nextPage = driver.findElement(By.linkText("Next »"));
		            Thread.sleep(1000);
		            //nextPage.click();
		            //Wait until new page loads
		            //linkStale(nextPage);
		            String nextPageURL = nextPage.getAttribute("href");
		            
		            driver.close();
		            driver = new ChromeDriver();
		            driver.get(nextPageURL);
			        title = driver.getTitle();
				}
	            writer.write("%end");
	            writer.close();
	            

        	} catch(Exception e) {
        		e.printStackTrace();
        	}
        }
        //close Chrome
        System.out.println("ALL DONE!");
        driver.close();
	}
	
	private static String getRating(WebElement review) {
		String revText = review.getText();
		int decimalIndex = revText.indexOf('.');
		System.out.println(decimalIndex);
		if(decimalIndex > -1) {
			revText = revText.substring(decimalIndex - 1, decimalIndex + 3);
		}
		return revText;
	}
}
