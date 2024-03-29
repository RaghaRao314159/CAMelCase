# Persona by CAMelCase


http://Juan289Flerovium.pythonanywhere.com/



<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/RaghaRao314159/CAMelCase">
    <img src="images/logo.jpeg" alt="Logo" width="300" height="300">
  </a>

  <h3 align="center">Persona</h3>

  <p align="center">
    An awesome personalised chat app!
    <br />
    <a href="https://devpost.com/software/persona-39m1u6"><strong>Hackathon Submission »</strong></a>
    <br />
    <br />
    <a href="https://github.com/RaghaRao314159/InnovAItio/blob/67b093642f285768981b217163e14a1c2477aebe/InnovAItio.pdf">Read More
    .
    <a href="https://github.com/RaghaRao314159/InnovAItio/blob/83e41ee12fd818c32c4d18c0288a21263f1761c8/InnovAItio%20Demo.mp4">View Demo</a>
    ·
    <a href="https://github.com/RaghaRao314159/InnovAItio/blob/67b093642f285768981b217163e14a1c2477aebe/peresentation.mp4">View Presentation</a>
    .
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](http://Juan289Flerovium.pythonanywhere.com/)

### Current problems with chat apps:
* Sending voice messages may not always be convenient. Text messages remain the main form of online communication today.
* Texts lack the ability to effectively capture the depth and nuances of communication.
* Visually impaired individuals are unable to read text messages. Text readers read these messages in a monotone manner, not delivering an accurate representation of the message.
* My mother recently reached the age where she requires reading glasses every time she opens WhatsApp. She will be the first to benefit from this app
     
This chat app solves these problems by adding the human element to text messages. The text messages sent by your mother (for e.g.) can be heard in your mother's voice.

### Why Persona?:
* The visually impared will finally feel empowerd and included in individual and group chats.
* Prevents miscommunication.
* Provide a much more personalised experience to mundane text messaging.

### How to use?:
1. Get a 30s recording of your friend, (e.g. Sam)
2. Save Sam in your phone contacts - name, number, description
3. Save Sam's voice in Persona app 
4. Go to chat and hear Sam's text in Sam's voice.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Elevenlabs][Elevenlabs]][Elevenlabs-url]
* [![Flask][Flask]][Flask-url]
* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To use the app, [click here](https://ragharao.pythonanywhere.com/) \\
To get a local copy up and run, follow these simple example steps.

### Prerequisites

Install these libraries
* npm
  ```sh
  pip install --upgrade Flask
  pip install elevenlabs
  ```

### Installation


1. Get a free Elevenlabs API Key at https://elevenlabs.io/subscription
2. Clone the repo
   ```sh
   git clone https://github.com/RaghaRao314159/CAMelCase.git
   ```
4. Enter your API in `Persona/model.py`
   ```py
   set_api_key('ENTER YOUR API KEY');
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run flask_app.py in the Web_Innovatio directory. 
 ```sh
   python flask_app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

### Features
- [x] Text-to-voice
- [x] Saving Contacts 
- [ ] Add personalised instructional voice support for the visually impaired
- [ ] Add emoji and GIF support
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

### Marketing
- [ ] Pilot test with visually impaired communities
    - [ ] The World Blind Union
    - [ ] Singapore Association of the visually handicapped

### Pay wall
- [ ] Pro plan
    - [ ] Add more individuals in Contacts
    - [ ] $3 USD monthly subscription

See the [info pack](https://github.com/RaghaRao314159/InnovAItio/blob/67b093642f285768981b217163e14a1c2477aebe/InnovAItio.pdf) for a full run down of our plan

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Ragha Rao - ragharao2001@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Logo from DALL.E 2 Open AI](https://openai.com/dall-e-2)
* [Presentation made using Canva](https://www.canva.com)
* [Website hosted on Pythonanywhere](https://www.pythonanywhere.com)
* [Hackathon by Lablab.ai](https://lablab.ai)
* [AI by Elevenlabs](https://elevenlabs.io/speech-synthesis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/RaghaRao314159/InnovAItio.svg?style=for-the-badge
[contributors-url]: https://github.com/RaghaRao314159/InnovAItio/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/RaghaRao314159/InnovAItio.svg?style=for-the-badge
[stars-url]: https://github.com/RaghaRao314159/InnovAItio/stargazers
[issues-shield]: https://img.shields.io/github/issues/RaghaRao314159/InnovAItio.svg?style=for-the-badge
[issues-url]: https://github.com/RaghaRao314159/InnovAItio/issues
[product-screenshot]: images/screenshot.jpg
[Elevenlabs]: https://img.shields.io/badge/11ElevenLabs-ff0000
[Elevenlabs-url]: https://elevenlabs.io/speech-synthesis
[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.3.x/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org
[Javascript]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[Javascript-url]: [https://vuejs.org/](https://www.javascript.com)
[html]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[html-url]: https://html.com
[jinja]: https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black
[jinja-url]: https://jinja.palletsprojects.com/en/3.1.x/
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
