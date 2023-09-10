# SWEtooth Candy Co. Shop
[SWEtooth Candy Co. Shop](https://swetooth-candy-co-c66a5c7b1ddf.herokuapp.com/) is an online candy store that brings the joy of Swedish confectionery right to your doorstep.
Whether creating your own candy mix or choosing from our pre-mixed selection, you're sure to find something sweet to your liking.

![Am-I-Responsive mockup](static/images/readme/pp5-responsive.png)

## Table of Contents
?TABLE OF CONTENTS:

## UX

### User Demographic

SWEtooth Candy Shop was built for candy enthusiasts of all ages, adults looking for a taste of nostalgia, young adults celebrating special occasions or curious individuals simply looking to explore Swedish candy traditions.
For those wanting to share some sweetness, the store also offers gift solutions such as gift wrapping/boxes/baskets to turn their order into a delightful gift worth remembering.

### User Stories

The full project board can be found [here](https://github.com/users/AndreeeasN/projects/2)

#### As a visitor
- I can sign up so that I can store my order confirmations / billing info on my account
- I can recover my password so that I can keep using my account if I lose the password
- I can view specific categories so that I can easily find products I'm interested in without searching
- I can view product details so that I can see more information about my potential purchase
- I can select varying bag sizes so that I can order the amount I want
- I can add products to the cart so that I can purchase several products at once
- I can checkout the contents of my cart so that I can pay and receive my products

#### As an admin
- I can add/delete products so that the store can adjust what's being sold
- I can edit products so that the store can adjust product details
- I can sort through the admin menu so I can quickly find what I'm looking for

### Colour Scheme:
?COLOR SCHEME:

### Typography:
?FONTS USED:

## Wireframes
- Home page<br>
![Home page](static/images/readme/pp5-wireframe-index.png)
- Products page<br>
![Products page](static/images/readme/pp5-wireframe-products.png)
- Product Details page<br>
![Product Details page](static/images/readme/pp5-wireframe-details.png)
- Cart page<br>
![Cart page](static/images/readme/pp5-wireframe-cart.png)
- Checkout page<br>
![Checkout page](static/images/readme/pp5-wireframe-checkout.png)


## Database Schema
?ERD:


## Features

### Existing Features

#### Navigation
![Navbar logged in](static/images/readme/pp5-nav-logged-in.png)<br>
- Header logo
    - Brings user to the home page on click
- Search bar
    - The Search bar allows the user to search for products by their name, description and product tags<br>
    ![Search bar]()
    - The search function is accessible from all pages, and the search results are displayed on the products page.
    - On smaller screens the search bar will be moved into the sidenav to save space.
- Mobile Navbar
    - On smaller screens the navigation bar only contains 3 elements: Browse, Login and Cart.
    - All hidden navigational elements are available from the Sidenav which can be opened using the "Browse" button
- Sidenav<br>
    ![Sidenav]()
    - The side navigation can be opened by clicking "Browse by Category" from the desktop navigation bar, or the "Browse" button on mobile.
    - The sidenav contains all categories and a few subcategories.
    - All links lead to the products page using different category/tag/search criteria.
- Log in / Sign up<br>
    ![Navbar logged out]()
    - When not logged in displays a link to log in or sign up
- Profile Name<br>
    ![Navbar dropdown]()
    - When logged in displays a dropdown menu where your user profile and log out button can be found.
    - If logged in as a superuser the "Add product" page and Admin Menu can be accessed from here.
- Cart<br>
    ![Cart]()
    - Takes user to their cart on click
    - If cart currently contains items a red notification will be display the amount
        - "Cart" will also be replaced with the total of all contained items
- Back-to-top Button<br>
    ![BTT button]()
    - When scrolling a certain distance on longer pages, a button appears in the bottom right corner
        - Pressing this button will scroll back to the top of the page, helping the user should they want to scroll back to the top

#### Main Page
- Hero Image / Carousel<br>
    ![Carousel]()
    - A simple Bootstrap 5 carousel featuring 3 different images that can be scrolled through.
    - All images are clickable and lead to relevant pages.
    - Hidden on smaller screen sizes.
- Featured Content<br>
    ![Featured Content]()
    - 3 cards featuring an image and some information about candy / available products.
    - All cards contain a link to their relevant pages

#### Products Page

- Products<br>
    ![Products]()
    - Products are displayed in grid pattern showing the product's name and price
    - Each product has it's own "Add to cart" button
        - If the product has sizes / variants this will be replace with a "Choose Options" button that leads to the relevant product details page where a size can be chosen.
    - If logged in as superuser each product will have 2 extra options:
        - "Edit" - Allows the user to change details about the product (Name, price, category, brand, tags, sizes, image etc.)
        - "Delete" - Removes the product from the database entirely
- "Sort By" Dropdown<br>
    ![Sort By]()
    - Allows the user to sort their search by name and price, either ascending or descending
    - Displays how many products are present in the current category/search
- Pagination<br>
    ![Pagination]()
    - When the amount of products in a category/search exceeds a maximum they are split into pages and a page selection bar is displayed at the bottom of the products page.
    - The page selector allows the following actions:
        - Jump one page forward / back
        - Jump to the first / last page
        - Jump to a page within 3 pages of the current one

#### Product Details Page
- Product details<br>
    ![Product details page]()
    - Displays detailed information about the specified product
        - Product image, name, price, quantity selector, description and "Add to cart" are always visible
        - Size/variant selector only displayed when product has sizes/variants available
            - On selecting a variant the product price label will update to reflect this change
    - If logged in as superuser the page will have 2 extra options:
        - "Edit" - Allows the user to change details about the product (Name, price, category, brand, tags, sizes, image etc.)
        - "Delete" - Removes the product from the database entirely

#### Cart Page
- Your Cart<br>
    ![Your Cart]()
    - Displays all items the user has added to their cart
        - Each product displays the following:
            - Name, SKU, price, quantity and subtotal
            - If product has a size/variant it will also be displayed
        - The quantity of each item can be adjusted using the - and + buttons followed by "Update"
        - The "Remove" link will entirely remove the product from the cart
    - Tallies up the cost of all products and displays at the bottom
        - The grand total includes delivery fee
            - If the total exceeds a certain threshold the delivery will be free
    - The checkout button takes the user to the Checkout page
    - "Continue shopping" takes the user to the Products page
 
 #### Checkout Page
 - Checkout<br>
    ![Checkout]()
    - Form containing billing details, delivery address and payment information for completing the transaction
        - Form has a checkbox to save delivery information to user profile
            - Saved delivery information can be changed from user profile
            - Replaced with text to sign up/log in if not logged in
    - Displays simple order summary of all cart items and the grand total
    - "Adjust Cart" takes user back to the Cart page
    - The "Complete Order" button uses the form information to attempt a monetary transaction through Stripe.
        - On succesful payment the user is shown an order confirmation that is also sent to their registered email.<br>
        ![Order Confirmation]()

#### User Account
- My Profile<br>
    ![Profile]()
    - Displays a form containing delivery information if entered by user.
        - This information will auto-fill the form for delivery information during checkouts
    - Also provides a list of previous orders
        - By clicking the order number the user may see the full order confirmation<br>
        ![Order Confirmation]()
- Sign in<br>
![Sign in page]()
- Sign up<br>
![Sign up page]()
- Sign out<br>
![Sign out page]()

### Future Features
- Tag dropdown in product search
- Make "Update" quantity in cart automatic
- "About" page
- FAQ page


## Testing

### Manual Testing

#### 1. Navbar
- Responsiveness
    - Resizes well down to a minimum screen width of 320px
    - On smaller screen sizes the search bar will be moved to sidenav as intended
- Website logo
    - Redirects to the front page as intended.
- Search bar
    - Redirects to products page as intended.
    - Includes name, description and tags specified to be visible in searches as intended.
    - On searching without text entered shows "No search text entered" and redirects to product page as intended.
- Navigational links
  - All links change color on hover as expected
    - Applies to mobile view elements as well
  - "Browse" and "Browse by Category" both open the sidenav as intended
  - All other links redirect to their intended urls
- Log in
  - Redirects to the login page as intended.
  - Visible only when not logged in as intended.
  - Icon is correctly replaced with a solid version when logged in.
  - Link is correctly replaced with the User dropdown menu when logged in.
- User Dropdown menu
    - All links redirect to their intended urls
    - Displays currently logged in User's username as intended.
    - Correctly hides 'Add new Product' and 'Django Admin Menu' when not logged in as a superuser

#### 2. Home page
- Responsiveness
    - Resizes well down to a minimum screen width of 320px
    - On smaller screen sizes the hero images/carousel is hidden as it doesn't scale well and images + their text aren't visible enough to warrant the screen real estate.
    - On smaller screen sizes the featured content cards will stack vertically
- Hero Image / Carousel
    - ?REQUIRES TESTING
- Featured Content
    - All buttons redirect to their intended Urls
- Back-to-top button
    - Appears upon scrolling down as intended
    - Disappears upon scrolling back up as intended
    - Z-index puts button on top of other elements when visible as intended

#### 3. Products Page
- Responsiveness
    - Resizes well down to a minimum screen width of 320px
    - On smaller screen sizes the pagination bar will wrap around if many pages are available
- Header  
    - Correctly displays header as the currently viewed category
    - Shows "Search results" on search as intended
- Products
    - Clicking on a product image or name redirects to it's details page as intended
    - "Add to Cart" correctly adds the item to the user cart
        - Products with size selection correctly changes button to "Choose Options" that redirect to the product details page
    - When logged in as superuser the options to edit and remove correctly redirect to their respective Urls
        - If not logged in redirects to login page as intended
        - If logged in but not a superuser, redirects to home page with warning message as intended
- "Sort By" dropdown
    - Correctly displays the amount of products displayed
    - Sorts both by name/price, both ascending and descending correctly
- Pagination
      - Enumerated page selector
        - Correctly displays and highlights the current page
        - Correctly redirects to intended page number on click
      - 'Next' and 'Previous' buttons
        - Correctly jumps forward or back one page on click
        - Correctly hides if on the first / last page
      - 'First' and 'Last' buttons
        - Correctly jumps to the first / last available page on click
        - Correctly hides if on the first/last page

#### 4. Product Details Page
  - Responsiveness
    - Resizes well down to a minimum screen width of 320px
    - On smaller screen sizes the product image will stack on top of the product information
  - Product information
    - Product image, name, price and description all display correctly
    - Products with sizes/variants correctly display a dropdown selection menu
      - Product price label correctly updates on changing variant
  - Quantity selection
    - '+' and '-' buttons increase and decrease quantity accordingly
      - The value is correctly clamped between 1-99
    - If a manually entered value exceeds 99 it'll be set to 99 as expected
    - If manually entered value isn't a valid integer the value will correctly be set to 1
  - Add to cart
    - Correctly adds the selected quantity and variant to cart and refreshes the page
    
#### 5. Cart Page
  - Responsiveness
    - Resizes well down to a minimum screen width of 320px
    - On smaller screen sizes the product images are hidden
  - Product information
    - Product image, name, price, SKU and subtotal all display correctly
    - Products with sizes/variants correctly display underneath the product name
      - The product price is correctly replaced with the variant price
    - If no products in cart, correctly displays "Empty" message
  - Quantity selection
    - '+' and '-' buttons increase and decrease quantity accordingly
      - The value is correctly clamped between 1-99
    - If a manually entered value exceeds 99 it'll be set to 99 as expected
    - If manually entered value isn't a valid integer the value will correctly be set to 1
  - "Update"
    - Correctly updates the quantity of selected product and refreshes page
  - "Remove"
    - Correclty removes product from cart and refreshes page
  - "Continue Shopping" link
    - Correctly redirects to products page
  - Grand total
    - The delivery fee (10%) is correctly added to the total to make the grand total
    - If total exceeds the set threshold the delivery fee is set to €0 as intended
  - Checkout
    - Correctly redirects to checkout page

#### 6. Checkout Page
  - Responsiveness
    - Resizes well down to a minimum screen width of 320px
    - On smaller screen sizes the order summary is stacked on top of the checkout form
  - Product information
    - Product image, name, quantity and subtotal all display correctly
    - Products with sizes/variants correctly display underneath the product name
    - If no products in cart, redirects to main page with a warning message as intended
  - Grand total
    - The delivery fee (10%) is correctly added to the total to make the grand total
    - If total exceeds the set threshold the delivery fee is set to €0 as intended
  - Checkout form
    - Auto-fills fields with user delivery information as intended
    - Only fields marked with * are required as intended
    - Country dropdown default field is marked as gray as intended
    - "Save this delivery information" checkbox correctly saves delivery information to user profile on checkout
  - Complete Order
    - On successful payment correctly redirects to order confirmation
      - The order confirmation is also sent to the entered email
        - ?REQUIRES TESTING
      - "Return to Home Page" redirects to home page as intended

#### 7. 'Add / Edit Product' pages
  - Authorization
    - Correctly redirects user to login page if not logged in when entering page
    - Correctly redirects user to login page if attempting to submit after logging out in a separate tab
    - Redirects user to home page if logged in user is not superuser or owner of the post
  - Product form
    - Correctly auto-fills fields with pre-existing information 
  - 'Submit Thought' button
    - Correctly submits thought form and updates/creates product
    - Redirects to affected product as intended
  
#### 8. Sign up Page
  - Responsiveness
    - Resizes well down to a minimum screen width of 320px
  - Authorization
    - Redirects user to main page if already logged in
  - Sign up form
    - Correctly allows signing up both with or without entering an E-mail
    - Correctly disallows signing up under the following conditions:
      - Missing Username or Password
      - Password too short
      - Password too common
      - Password contains username
      - Repeated password doesn't match first password
  - 'Sign In' link
    - Correctly redirects to sign in page

#### 9. Sign in Page
  - Responsiveness
    - Resizes well down to a minimum screen width of 320px
  - Authorization
    - Redirects user to main page if already logged in
  - Sign in form
    - Correctly allows signing in using the corrects username and password
    - Correctly disallows submitting without a username or password
  - 'Sign Up' link
    - Correctly redirects to sign up page

#### 10. Sign out Page
  - Responsiveness
    - Resizes well down to a minimum screen width of 320px
  - Authorization
    - Redirects user to main page if already logged out
  - 'Sign Out' button
    - Correctly logs the user out
    - Redirects user to main page as intended

#### 12. 404 Page
  - Responsiveness
    - Resizes well down to a minimum screen width of 320px
  - 'Return Home' button
    - Correctly redirects user to main page

#### 13. Footer
  - Responsiveness
    - Resizes well down to a minimum screen width of 320px
    - On small-medium screen sizes the disclaimer and social links stack vertically as intended
  - Social links
    - Correctly change color on hover
    - The GitHub link opens in a new tab as intended
    - The LinkedIn link opens in a new tab as intended

### Discovered Bugs
- The bootstrap offcanvas backdrop was covering every element, including the actual offcanvas.
  - This was due to the offcanvas using a modal-backdrop which has a z-index of 1050 whereas the offcanvas had a lower z-index of 1045.
    - This bug was fixed in a newer version of bootstrap 5 and as such has been updated.

- Attempting to search for products using the search bar would throw the exception: TypeError at /products/ - object of type 'method' has no len() during search
  - This was caused by a typo in the search filter, using "distinct" instead of the method "distinct()"

- On the cart and checkout page, the subtotal was incorrectly calculated for items without variants.
  - This was due to a wrongly assigned variable in the cart items context, setting the price to product.price rather than the variable "price"

- Searching for products in the django admin menu would throw an exception
  - This was due to one of the search fields being ['brand'] rather than ['brand__name'], returning a model rather than the brand name

- The add/edit/remove product page displayed a "Not authorized" message but didn't actually redirect unathourized users
  - This was due to missing "return redirect()" and instead just "redirect()" in the products view
