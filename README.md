# Tray.io March 2021 Hackathon

## Objective:
6 main SaaS performance indicators were provided by Tray.io to be analyzed:

- Analyst Value (0 - 5)
- Partner Value (0 - 5)
- Persona Value (0 - 5)
- Growing market
- Organic Search Volume
- SEO Value (0 - 3)

The objective was to identify which of these features mattered most for determining SaaS "Unicorn" 🦄 API's that they would want to integrate into their business package.

## Methodology:

We wanted to create a model that predicts and potentially improves the decision making process. To do so we extracted the list of already served API's and combined this with the existing data (resulting in 34 matches) to identify patterns/trends in their API choices. 

We then used a K-means clustering model to identify trends in Tray's SaaS API choices for their package and then created recommendations for potential company choices that their business model might be overlooking. Specifically we felt a potential expansion currently not targeted by Tray would be to introduce SaaS companies into their package that have:

- High analyst value
- High partner value
- Low persona value
- (Potential High SEO value; not required)

## APP:

App is not currently running in a network, to test please fork the repository and use the following command:
- streamlit run app.py

![image](https://user-images.githubusercontent.com/73958258/111911627-3d9a1880-8a5e-11eb-9087-2c126c2e488c.png)

![image](https://user-images.githubusercontent.com/73958258/111911654-5c98aa80-8a5e-11eb-8221-489439a606c7.png)

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for tray_hackathon in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/tray_hackathon`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "tray_hackathon"
git remote add origin git@github.com:{group}/tray_hackathon.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
tray_hackathon-run
```

# Install

Go to `https://github.com/{group}/tray_hackathon` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/tray_hackathon.git
cd tray_hackathon
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
tray_hackathon-run
```
