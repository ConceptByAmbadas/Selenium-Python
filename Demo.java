package com.info.TestRunner;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.ITestContext;
import org.testng.annotations.Test;

public class Demo {
	WebDriver driver;

	@Test
	public void UploadFileUsingSendKeys()
			throws InterruptedException {

		driver = new FirefoxDriver();
		String workingDir = System.getProperty("user.dir");
		String filepath = workingDir + "\\HTML_Pages\\demo.html";
		driver.get(filepath);

		WebElement fileInput = driver.findElement(By.name("uploadfile"));
		fileInput.sendKeys(filepath);

		// Added a wait to make you notice the difference.
		Thread.sleep(1000);

		driver.findElement(By.id("uploadfile")).sendKeys(
				"C:\\demo.txt");

		// Added sleep to make you see the difference.
		Thread.sleep(1000);

		fileInput.sendKeys(filepath);
	}
}
