USERNAME = "BizTecBritain"

pTitle = input("Page Title: ")
rTitle = input("Repo Title: ")
desc = input("Type description (i.e. A python program to solve the daily wordle): ")
licenseAdd = input("Add license? (y/n): ").lower() == "y"
licenseType = ""
licenseContents = ""
if licenseAdd:
    licenseAdd = "## License\n\nDistributed under the " + input("License Type (i.e. MIT): ") + " License. See `LICENSE` for more information."
    licenseContents = "\n    <li><a href=\"#license\">License</a></li>"

print(f"""




[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]



<br />
<p align="center">
  <a href="https://github.com/BizTecBritain">
    <img src="https://github.com/BizTecBritain/BizTecBritain/blob/main/BizTec.png" alt="Logo" width="580" height="300">
  </a>

  <h3 align="center">{pTitle}</h3>

  <p align="center">
    {desc}
    <br />
    <a href="https://github.com/{USERNAME}/{rTitle}/blob/main/docs/Usage.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/{USERNAME}/{rTitle}">View Demo</a>
    ·
    <a href="https://github.com/{USERNAME}/{rTitle}/issues">Report Bug</a>
    ·
    <a href="https://github.com/{USERNAME}/{rTitle}/issues">Request Feature</a>
  </p>
</p>



<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
    <li><a href="#contributing">Contributing</a></li>{licenseContents}
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



## About The Project

There is a new viral game called [wordle](https://www.powerlanguage.co.uk/wordle/).
As per usual I was bored and so i decided to try to program an algorithm to solve it for you!


### Built With

* Python version: 3.9 (Tested)
* Python version: 3.x



## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Install git and python
  ```
   $ sudo apt-get update
   $ sudo apt-get install git
   $ sudo apt-get install python
  ```

### Installation

Clone the repo with ```$ git clone https://github.com/{USERNAME}/{rTitle}.git```

Then enter the directory with ```$ cd {rTitle}```

## Usage

First verify you are in the correct directory, if not, run
```
$ cd {rTitle}
```

Then to use this code run
```
$ python {rTitle}.py
```

_For more examples, please refer to the [Documentation](https://github.com/{USERNAME}/{rTitle}/blob/main/docs/Usage.md)_



## Roadmap

See the [open issues](https://github.com/{USERNAME}/{rTitle}/issues) for a list of proposed features (and known issues).



## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



{licenseType}



## Contact

Alexander Bisland - Twitter: [@BizTecBritain](https://twitter.com/BizTecBritain) - Email: BizTecBritain@gmail.com

Project Link: [https://github.com/{USERNAME}/{rTitle}](https://github.com/{USERNAME}/{rTitle}) 



## Acknowledgements

* Thanks to [othneildrew](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md) for the blank README.md file

[contributors-shield]: https://img.shields.io/github/contributors/{USERNAME}/{rTitle}.svg?style=for-the-badge
[contributors-url]: https://github.com/{USERNAME}/{rTitle}/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/{USERNAME}/{rTitle}.svg?style=for-the-badge
[forks-url]: https://github.com/{USERNAME}/{rTitle}/network/members
[issues-shield]: https://img.shields.io/github/issues/{USERNAME}/{rTitle}.svg?style=for-the-badge
[issues-url]: https://github.com/{USERNAME}/{rTitle}/issues




""")

print("Don\'t forget to change the body of the page (About The Project to Usage and Contact)!")
