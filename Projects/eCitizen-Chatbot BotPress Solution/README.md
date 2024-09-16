# eCitizen Chatbot 


## Introduction 
The chatbot created was made on the botpress platform for the purpose of acting as a customer service assistance chatbot for eCitizen platform users. The client side of the chatbot is hosted on Facebook messenger  Link:[https://www.facebook.com/profile.php?id=61563415835290] while the server side of the chatbot is hosted on the Botpress server Link: [https://botpress.com/]. The project entails flowchart schematics for the main and QnA workflows drawn on draw.io software, screenshots for workspace as well as chatbot features available on the botpress platform, a list of websites stored in the AI-Knowledgebase as well as the AI-Logic Script, Identity and Access Management logs as well as details on the chatbot setup and use. 


# **Chatbot Requirements and Setup**

## **Client Side: Facebook Messenger**

### **Requirements**

1. **Facebook Developer App Dashboard**
   - **AppID**: Unique identifier for your Facebook app.
   - **App Secret**: Confidential key used to authenticate your app.
   - **Display Name**: The name of your app as it will appear to users.
   - **Contact Email**: Email address for contact purposes.

2. **Messenger API Setup**
   - **Configure Webhooks**: Set up webhooks to allow Facebook to communicate with your server.
   - **Generate Access Token**: Create an access token to authenticate API requests.
   - **Complete App Review**: Submit your app for Facebook's review to ensure it complies with their policies.

### **Setup Procedure**

#### 1. Create a Facebook App
- Go to the [Facebook Developers](https://developers.facebook.com/) site.
- Navigate to the App Dashboard and click on **"Create App"**.
- Choose **"For Everything Else"** and click **"Continue"**.
- Fill in the **App Name**, **Contact Email**, and other required fields.
- Click **"Create App ID"** and complete any security checks.

#### 2. Configure App Settings
- In the App Dashboard, go to **Settings** > **Basic**.
- Note your **App ID** and **App Secret**. You’ll need these for the server-side setup.
- Fill in the **Display Name** and **Contact Email** if not already done.
- Click **"Save Changes"**.

#### 3. Set Up Messenger API
- In the App Dashboard, go to **Add a Product** and select **"Messenger"**.
- Under the **Messenger** section, click **"Set Up"**.
  
  **Configure Webhooks**:
  - Click **"Webhooks"** under the **Messenger** product.
  - Add your webhook URL and verify the token.
  - Subscribe to the events you want to receive (e.g., messages, postbacks).

  **Generate Access Token**:
  - In the **Messenger** settings, go to **"Token Generation"**.
  - Select the page for which you want to generate a token and click **"Generate Token"**.
  - Copy the token and store it securely.

  **Complete App Review**:
  - Go to **App Review** in the App Dashboard.
  - Submit your app for review if you need permissions beyond the default ones.
  - Follow Facebook’s instructions to complete the review process.

---

## **Server Side: Botpress Servers**

### **Requirements**

1. **Integrations Section of the Workspace**
   - **AppID**: From your Facebook app settings.
   - **App Secret**: From your Facebook app settings.
   - **Verify Token**: The token you used when setting up the webhook on Facebook.
   - **Page ID**: The ID of the Facebook page your bot will interact with.
   - **Access Token**: The token generated for your Messenger API.

### **Setup Procedure**

#### 1. Access Botpress Workspace
- Log in to your Botpress platform.
- Go to the workspace where you want to set up the Facebook Messenger integration.

#### 2. Configure Facebook Messenger Integration
- Navigate to the **Integrations** section of your workspace.
- Click on **"Add Integration"** or **"Configure"** under the Facebook Messenger integration.
- Enter the following details:
  - **AppID**: Paste the App ID from the Facebook Developer App Dashboard.
  - **App Secret**: Paste the App Secret from the Facebook Developer App Dashboard.
  - **Verify Token**: Enter the token you used when configuring the webhook on Facebook.
  - **Page ID**: Paste the Page ID of the Facebook page.
  - **Access Token**: Paste the access token generated in the Facebook Messenger API setup.

#### 3. Save and Test
- Save your configuration in Botpress.
- Test the integration by sending a message to your Facebook page and verifying that it is received by your Botpress bot.

#### 4. Deploy and Monitor
- Once tested, deploy your chatbot and monitor its performance.
- Make any necessary adjustments based on feedback and usage.

#### Links 
Incase of any queries kindly refer to the botpress and facebook documentation links
Link1: https://developers.facebook.com/docs
Link2: https://botpress.com/docs/messenger



# Chatbot Testing and Use on Facebook Messenger

## **Prerequisites**

- **Facebook Account**: Ensure that the tester has an active Facebook account.
- **Developer Role Assignment**: Tester must be granted a role in the Facebook Developer App.
- **Botpress Workspace Access**: Tester needs to be added to the Botpress workspace for server-side access.

## **Steps for Testing the Chatbot**

### **1. Request Access from the Developer**

- Contact the developer and request access to the Facebook app for testing.
- Provide Facebook account details (name or email) to the developer.

### **2. Developer Adds Tester to the Facebook App**

- **Log in to the Facebook Developer Portal**.
- **Navigate to App Roles**: Go to **Roles** > **Testers** in the App Dashboard.
- **Add the Tester**: Enter the tester’s Facebook account details and assign a role.

### **3. Accept the Tester Role Invitation**

- Tester receives a notification or email.
- **Accept the Invitation**: Click on the link and follow the instructions to accept the role.

### **4. Test the Chatbot on Facebook Messenger**

- **Open Facebook Messenger**.
- Search for the chatbot using the page name.
- **Interact with the Chatbot**: Start a conversation and test its responses.

### **5. Developer Adds Tester to the Botpress Workspace**

- **Invite the Tester**:
  - Go to the Botpress workspace and navigate to **Members**.
  - Click **Invite Member** and enter the tester’s email.
- **Assign Permissions**: Select appropriate permissions and send the invitation.

### **6. Tester Accesses the Botpress Workspace**

- **Accept the Invitation**: Tester receives an email invitation to join the workspace.
- **Log in to Botpress**: Follow the email link to access the workspace.

## **Important Notes**

- **Limited Access**: Only those with a role in the Facebook Developer App can interact with the chatbot, as the app hasn’t been reviewed.
- **App Review**: Consider submitting the app for review to enable broader testing.

---

This format should make the documentation easy to follow while being visually appealing when viewed in Markdown.



