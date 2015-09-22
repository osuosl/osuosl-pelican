PowerLinux / OpenPOWER Request Form
===================================
:slug: services/powerdev/request_hosting
:title: PowerLinux / OpenPOWER Request Form
:order: 19
:menu_parent: t4s2

.. raw:: html

    <div id="content">
    <!-- Formsender error script -->
    <script src="../../../theme/js/formsender-error.js"></script>
      <div class="field field-name-body field-type-text-with-summary field-label-hidden">
        <div class="field-items">
          <div class="field-item even" property="content:encoded">
            <p>Please use the form below to request hosting on the POWER7/POWER8 environment hosted at the OSUOSL.</p>
            <p>This access is intended only for projects who qualify and are approved by both the OSUOSL and IBM.</p>
          </div>
        </div>
      </div>
      <form class="webform-client-form" enctype="multipart/form-data" action="http://formsender.osuosl.org:80" method="post" id="webform-client-form-1086" accept-charset="UTF-8">
        <div>
          <div class="form-item webform-component webform-component-textfield" id="webform-component-name">
            <label for="edit-submitted-name">Name <span class="form-required" title="This field is required.">*</span></label>
            <input type="text" id="edit-submitted-name" name="name" value="" size="60" maxlength="128" class="form-text required" />
          </div>
          <div class="form-item webform-component webform-component-email" id="webform-component-email">
            <label for="edit-submitted-email">Email <span class="form-required" title="This field is required.">*</span></label>
            <input class="email form-text form-email required" type="email" id="edit-submitted-email" name="email" size="60" />
          </div>
          <div class="form-item webform-component webform-component-textfield" id="webform-component-project-name">
            <label for="edit-submitted-project-name">Project Name <span class="form-required" title="This field is required.">*</span></label>
            <input type="text" id="edit-submitted-project-name" name="project_name" value="" size="60" maxlength="128" class="form-text required" />
            <div class="description">Name of the open source project or education institution this request will be supporting.</div>
          </div>
          <div class="form-item webform-component webform-component-textfield" id="webform-component-community-size">
            <label for="edit-submitted-community-size">Estimated Size of  User Community <span class="form-required" title="This field is required.">*</span></label>
            <input type="text" id="edit-submitted-community-size" name="community_size" value="" size="60" maxlength="128" class="form-text required" />
            <div class="description">How many estimated users do you have in your community?</div>
          </div>
          <div class="form-item webform-component webform-component-textarea" id="webform-component-mission">
            <label for="edit-submitted-mission">Description of Project Mission <span class="form-required" title="This field is required.">*</span></label>
            <div class="form-textarea-wrapper resizable"><textarea id="edit-submitted-mission" name="project_mission" cols="60" rows="5" class="form-textarea required"></textarea></div>
            <div class="description">Please describe in detail the mission and purpose of this request in regards to how the POWER architecture will support your project. Also describe the general mission of your project.</div>
          </div>
          <div class="form-item webform-component webform-component-textarea" id="webform-component-usage">
            <label for="edit-submitted-usage">Expected usage model <span class="form-required" title="This field is required.">*</span></label>
            <div class="form-textarea-wrapper resizable"><textarea id="edit-submitted-usage" name="expected_usage_model" cols="60" rows="5" class="form-textarea required"></textarea></div>
            <div class="description">What types of activity will the machine be used for? (i.e. compile builds, performance testing, architecture troubleshooting, etc).</div>
          </div>
          <div class="form-item webform-component webform-component-textfield" id="webform-component-duration">
            <label for="edit-submitted-duration">Anticipated duration of need <span class="form-required" title="This field is required.">*</span></label>
            <input type="text" id="edit-submitted-duration" name="duration_of_need" value="" size="60" maxlength="128" class="form-text required" />
            <div class="description">How long do you expect you will need these resources? Ongoing or indefinitely are also acceptable answers.</div>
          </div>
          <div class="form-item webform-component webform-component-select" id="webform-component-power-architecture">
            <label for="edit-submitted-power-architecture">POWER Architecture <span class="form-required" title="This field is required.">*</span></label>
            <select id="edit-submitted-power-architecture" name="power_architecture" class="form-select required">
              <option value="None selected" selected="selected">- Select -</option>
              <option value="ppc64 POWER7">ppc64 POWER7</option>
              <option value="ppc64 POWER8 (Big Endian)">ppc64 POWER8 (Big Endian)</option>
              <option value="ppc64le POWER8 (Little Endian)">ppc64le POWER8 (Little Endian)</option>
            </select>
          </div>
          <div class="form-item webform-component webform-component-select" id="webform-component-flavor">
            <label for="edit-submitted-flavor">Flavor <span class="form-required" title="This field is required.">*</span></label>
            <select id="edit-submitted-flavor" name="flavor" class="form-select required">
              <option value="None selected" selected="selected">- Select -</option>
              <option value="m1_small">1 CPU, 2G RAM, 20G Disk</option>
              <option value="m1_medium">2 CPU, 4G RAM, 40G Disk</option>
              <option value="m1_large">4 CPU, 8G RAM, 80G Disk</option>
              <option value="m1_xlarge">8 CPU, 16G RAM, 160G Disk</option>
            </select>
          </div>
          <div class="form-item webform-component webform-component-number" id="webform-component-num-nodes">
            <label for="edit-submitted-num-nodes">Number of nodes <span class="form-required" title="This field is required.">*</span></label>
            <input type="number" id="edit-submitted-num-nodes" name="num_nodes" value="1" min="1" step="any" class="form-text form-number required" />
            <div class="description">Estimated number of nodes (machines) you'd like to have.</div>
          </div>
          <div class="form-item webform-component webform-component-select" id="webform-component-distribution">
            <label for="edit-submitted-distribution">Distribution <span class="form-required" title="This field is required.">*</span></label>
            <select id="edit-submitted-distribution" name="distribution" class="form-select required">
              <option value="None selected" selected="selected">- Select -</option>
              <option value="Fedora">Fedora</option>
              <option value="Debian">Debian</option>
              <option value="Ubuntu">Ubuntu</option>
              <option value="OpenSUSE">OpenSUSE</option>
              <option value="Other">Other</option>
            </select>
            <div class="description">Which Linux distribution would you like to use for your machine? This would likely be the latest stable version available for PPC. If you want a specific version, please state that in the comments section on the last page.</div>
          </div>
          <div class="form-item webform-component webform-component-select" id="webform-component-openstack-access">
            <label for="edit-submitted-openstack-access">OpenStack Access </label>
            <select id="edit-submitted-openstack-access" name="openstack_access" class="form-select">
              <option value="None selected" selected="selected">- None -</option>
              <option value="Have the OSL create the node(s) for me">Have the OSL create the node(s) for me</option>
              <option value="I'd like to have access to the Openstack GUI/API">I&#039;d like to have access to the Openstack GUI/API</option>
            </select>
            <div class="description">We use OpenStack to manage the POWER8 ppc64/ppc64le nodes. We can either create the node for you or we can grant you access to the OpenStack GUI and API and let you manage it yourself. What do you prefer?</div>
          </div>
          <div class="form-item webform-component webform-component-textarea" id="webform-component-ssh-key">
            <label for="edit-submitted-ssh-key">SSH Public Key <span class="form-required" title="This field is required.">*</span></label>
            <div class="form-textarea-wrapper resizable"><textarea id="edit-submitted-ssh-key" name="ssh_key" cols="60" rows="5" class="form-textarea required"></textarea></div>
            <div class="description">Public SSH key to be used for initial access to the system.</div>
          </div>
          <div class="form-item webform-component webform-component-textfield" id="webform-component-ibm-ltc-advocate">
            <label for="edit-submitted-ibm-ltc-advocate">IBM Linux Technology Center Advocate <span class="form-required" title="This field is required.">*</span></label>
            <input type="text" id="edit-submitted-ibm-ltc-advocate" name="ibm_LTC_advocate" value="" size="60" maxlength="128" class="form-text required" />
            <div class="description">If you do not have an IBM Advocate, one will need to be assigned prior to activating access. OSUOSL and IBM will work with the requesting project to find an appropriate advocate.</div>
          </div>
          <div class="form-item webform-component webform-component-select" id="webform-component-deployment-timeframe">
            <label for="edit-submitted-deployment-timeframe">Deployment timeframe </label>
            <select id="edit-submitted-deployment-timeframe" name="deployment_timeframe" class="form-select">
              <option value="Within 7 business Days" selected="selected">Within 7 business Days</option>
              <option value="Within 3 business Days">Within 3 business Days</option>
              <option value="Within 1 business Days">Within 1 business Day</option>
            </select>
            <div class="description">Normal turnaround for access is typically 7 business days. If you need it sooner than that, please choose which time frame you need. We will do our best to accommodate your request. </div>
          </div>
          <div class="form-item webform-component webform-component-textarea" id="webform-component-other-information">
            <label for="edit-submitted-other-information">Other information </label>
            <div class="form-textarea-wrapper resizable"><textarea id="edit-submitted-other-information" name="other_information" cols="60" rows="5" class="form-textarea"></textarea></div>
            <div class="description">Is there anything additional you would like to provide for your request?</div>
          </div>

          <!-- Formsender Settings -->
          <input type="hidden" name="last_name" value="" />
          <input type="hidden" name="tokn" value="15674hsda//*q23%^13jnxccv3ds54sa4g4sa532323!OoRdsfISDIdks38*(dsfjk)aS" />
          <!-- The following must be set to http://www.osuosl.org/services/powerdev/request_hosting in production -->
          <input type="hidden" name="redirect" value="http://www.osuosl.org/services/powerdev/request_hosting" />
          <input type="hidden" name="mail_subject" value="FORM: New PowerLinux/OpenPOWER Hosting Request" />
          <!-- /Formsender Settings -->

          <div class="form-actions form-wrapper" id="edit-actions"><input type="submit" id="edit-submit" name="op" value="Submit" class="form-submit" /></div>
        </div>
      </form>
    </div>
