Using Variables in a Custom Drupal Theme
========================================
:date: 2014-10-01
:author: lucyw
:slug: using-variables-custom-drupal-theme
:img: variables-drupal-theme.jpg

At the Open Source Lab we host many of our sites as a Drupal multisite. This
means that we have several instances of Drupal using the same theme, and then we
can populate each site with different content as needed (for instance,
cass.oregonstate.edu and osuosl.org would be different websites with different
messages, but with Drupal they can look and act the same. Pretty neat!). Since
not all of our sites are used by the OSL (i.e. the Center for Applied Systems
and Software), I recently needed to make our logo and organization name into
variables so that the user could just upload an image and fill in a text box to
customize the site theme to their organization. Luckily, Drupal makes my job
pretty easy.

First, I created a file ``osuosl-setting.php``. Since our theme is titled
osuosl, there are some things I can hard-code under our company name and this
seemed like one of them. The first step to magic variabilization is to alter the
systems theme settings and the form that controls them. Drupal’s naming scheme
is a little wonky (as you end up with things like
``hook_field_attach_prepare_translation_alter()``), but in a roundabout way it
makes sense. To digress a bit into this topic, let’s break down the
``osuosl_form_system_theme_settings_alter`` name. The first part of Drupal’s
function names is the object that it is affecting. In this case, osuosl is the
name of our theme, and the theme is the thing we are trying to add something to
(you could also be trying to make changes to blocks, pages, hooks, and a variety
of other things). Then, within the theme we are modifying the ``form_system``.
This includes any forms that are default in the Drupal theme, such as the
settings  form found under Appearance->Theme->Settings. Next, as seen in the
previous example, we’re modifying the **theme settings** form. And finally, we
are **altering** the form (as opposed to creating it, deleting it or setting
variables within it). This is how we get to
``osuosl_form_system_theme_settings_alter``. It’s not intuitive, but Drupal has
excellent documentation to help you along. Now, on to some code!

.. code-block:: php

  <?php
  function osuosl_form_system_theme_settings_alter(&$form, $form_state){
  }
  ?>

Next, there are two variables that need to be added to the form. For each of
these, we need to add them to the ``theme_settings`` array, and then make them
into their own arrays to store all the necessary information about them.

.. code-block:: php

  <?php
      function osuosl_form_system_theme_settings_alter(&$form, $form_state){
          $form['theme_settings']['logo'] = array();
          $form['theme_settings']['site_name'] = array();
    }
  ?>

Now we’ll fill in some variables about the logo and name

.. code-block:: php

  <?php
  function osuosl_form_system_theme_settings_alter(&$form, $form_state){
      $form['theme_settings']['logo'] = array(
            '#type' => 'managed_file',
            '#title' => t('logo'),
            '#required' => TRUE,
            '#default_value' => theme_get_setting('logo'),
            '#upload_validators' => array(
                'file_validate_extensions' => array('git png jpg jpeg')
                )
            );
      $form['theme_settings']['site_name'] = array(
            '#type' => 'textfield',
            '#title' => t('site_name'),
            '#default_value' => theme_get_setting('site_name')
            'required' => TRUE,
            );
  }
  ?>

Now that osuosl-settings.php was done and my variables were ready to be put into
the theme, I needed to add some defaults for them so that if the user didn’t
upload a logo or org name, there would still be something there. I decided to
use the OSL logo and organization name under the assumption that the theme will
be used primarily by us. So in ``osuosl.info``, I added the lines:

.. code-block:: php

  settings[logo] = images/logo-full.png
  settings[site_name] = OSU Open Source Lab

Finally, I had to call my variables in the Drupal templates so that they would
be rendered when the site was built!

.. code-block:: html

  <a href="/"><img src="<?php print theme_get_setting('logo'); ?>" alt="<?php print (theme_get_setting('site_name'));?>" /></a>

Ta-da! Now, all the user has to do is go to Appearances->Theme->Settings to
upload a new logo and fill in their organization name!
